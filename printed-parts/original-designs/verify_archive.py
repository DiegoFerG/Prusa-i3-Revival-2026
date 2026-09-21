"""Verify preserved upstream bytes and basic STL syntax; requires only Python 3.

This does not test manifoldness, slicing or mechanical fit.
"""
import hashlib
import json
import math
from pathlib import Path
import re
import struct


def stl_bounds(data):
    if len(data) >= 84:
        count = struct.unpack_from('<I', data, 80)[0]
        if len(data) == 84 + 50 * count:
            if count == 0:
                raise ValueError('empty binary STL')
            vertices = []
            for normal_and_vertices in struct.iter_unpack('<12fH', data[84:]):
                if not all(math.isfinite(v) for v in normal_and_vertices[:12]):
                    raise ValueError('non-finite binary STL coordinate or normal')
                vertices.extend(normal_and_vertices[3:12])
        else:
            count = None
    else:
        count = None
    if count is None:
        text = data.decode('ascii')
        matches = re.findall(r'\bvertex\s+(\S+)\s+(\S+)\s+(\S+)', text)
        count = len(re.findall(r'\bfacet\s+normal\b', text))
        if not text.lstrip().startswith('solid') or 'endsolid' not in text:
            raise ValueError('invalid ASCII STL envelope')
        if not count or len(matches) != count * 3 or len(re.findall(r'\bendfacet\b', text)) != count:
            raise ValueError('incomplete ASCII STL triangles')
        vertices = [float(v) for triple in matches for v in triple]
        if not all(math.isfinite(v) for v in vertices):
            raise ValueError('non-finite ASCII STL coordinate')
    axes = [vertices[i::3] for i in range(3)]
    dimensions = [max(axis) - min(axis) for axis in axes]
    if any(d <= 0 for d in dimensions):
        raise ValueError('degenerate mesh bounding box')
    return count, dimensions


def main():
    root = Path(__file__).resolve().parent
    manifest = json.loads((root / 'manifest.json').read_text(encoding='utf-8'))
    expected = set()
    meshes = []
    for entry in manifest['files']:
        relative = entry['path']
        path = (root / relative).resolve()
        if not path.is_relative_to(root / 'upstream') or relative in expected:
            raise ValueError(f'Unsafe or duplicate manifest path: {relative}')
        expected.add(relative)
        data = path.read_bytes()
        if len(data) != entry['bytes'] or hashlib.sha256(data).hexdigest() != entry['sha256']:
            raise ValueError(f'Archive content differs: {relative}')
        if path.suffix.lower() == '.stl':
            triangles, bounds = stl_bounds(data)
            meshes.append((relative, triangles, bounds))
    actual = {p.relative_to(root).as_posix() for p in (root / 'upstream').rglob('*') if p.is_file()}
    if actual != expected:
        raise ValueError(f'Manifest coverage differs: {sorted(actual ^ expected)}')
    print(f'PASS: {len(expected)} file hashes and {len(meshes)} STL files.')
    for relative, triangles, bounds in meshes:
        print(f'{relative}: {triangles} triangles; bounds ' + ' x '.join(f'{d:.2f}' for d in bounds))


if __name__ == '__main__':
    main()
