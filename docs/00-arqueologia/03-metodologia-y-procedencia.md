# Metodología arqueológica y procedencia

Prusa i3 Revival 2026 trata la configuración original como evidencia técnica. El objetivo no es solo conseguir que la impresora vuelva a funcionar: también queremos poder explicar **qué había, cómo estaba construido, qué conservamos y por qué lo cambiamos**.

## Regla principal

**Documentar antes de desmontar.**

No limpiar, cortar cables, retirar etiquetas, modificar conectores ni desechar piezas antes de registrar su estado y procedencia.

## Niveles de certeza

Cada identificación técnica utilizará uno de estos estados:

- **CONFIRMADO** — visible en serigrafía/etiqueta o demostrado mediante medición.
- **PROBABLE** — la geometría y el contexto encajan, pero falta confirmación.
- **PENDIENTE** — no existe evidencia suficiente todavía.

Una identificación probable nunca debe convertirse silenciosamente en un hecho histórico.

## Procedencia

Cada objeto se asignará a una clase:

### PRINTER-AS-FOUND
Estaba físicamente instalado en la impresora cuando comenzó el proyecto.

### LOOSE-FOUND
Apareció suelto en cajas asociadas al antiguo material de impresión 3D. Puede ser repuesto, pieza retirada, experimento o material sin usar.

### DONATED-PURCHASED
Se sabe que fue comprado o donado en aquella época, pero no necesariamente utilizado en esta impresora.

### PERIOD-UNRELATED
Hardware contemporáneo encontrado junto al material, sin relación demostrada con la Prusa.

### REVIVAL-2026
Componente adquirido, fabricado o diseñado específicamente para la reconstrucción actual.

## Flujo de desmontaje futuro

Para cada subconjunto:

1. fotografía antes de tocarlo;
2. asignación de ID;
3. fotografía de conexiones y orientación;
4. retirada controlada;
5. limpieza;
6. medidas y referencias;
7. prueba mecánica/eléctrica si procede;
8. decisión: **REUSE / RESTORE / REPLACE / REDESIGN / ARCHIVE**;
9. registro de la decisión y motivo;
10. fotografía del componente ya clasificado.

## Seguridad

La impresora no se energizará simplemente para comprobar si todavía funciona. Fuente, red, cama, MOSFET, conectores, aislamiento y cableado deben inspeccionarse antes.

## Fotografía

Los originales son evidencia y permanecen inmutables. Las versiones para el blog, anotaciones y comparativas se generan como derivados.

## Trazabilidad

Las decisiones de diseño futuras deberán enlazar, cuando sea posible:

`evidencia original → medida/prueba → decisión → pieza CAD/BOM → resultado`

Esta cadena es una de las partes centrales del valor comunitario del proyecto.
