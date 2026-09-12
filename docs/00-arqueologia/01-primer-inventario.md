# Primer inventario arqueológico

Fecha: **12 de septiembre de 2026**

Este documento registra lo que puede identificarse visualmente antes de desmontar la impresora.

## Identificación provisional

Familia: **Prusa i3 clásica / Rework-era / RepRap derivative**.

La identificación exacta de variante queda pendiente de mediciones y comparación con documentación histórica.

## Elementos observados

### Estructura
- Marco vertical plano metálico.
- Base Y construida con varillas roscadas, tuercas y piezas impresas.
- Guías lineales sobre varilla lisa.

### Eje Z
- Dos motores NEMA17.
- Varillas lisas verticales como guías.
- Varillas roscadas convencionales como elementos de avance.
- Acoplamientos flexibles de aluminio entre motor y varilla roscada.

**Decisión Revival:** sustituir las varillas roscadas Z por husillos trapezoidales seleccionados después de medir geometría y definir avance.

### Extrusor
- Extrusor directo con reducción por engranajes, familia Wade / Greg's Wade.
- Gran rueda dentada impresa y piñón de motor.
- Sistema de presión mediante muelles.
- Configuración histórica compatible con filamento de 3 mm.

**Decisión Revival Phase 1:** intentar conservar/reconstruir esta arquitectura para consumir el stock Legacy 3 mm.

### Hotend
- El propietario recuerda que es un E3D.
- La nueva fotografía lateral muestra un disipador E3D-family claramente reconocible.
- Pendiente distinguir de forma concluyente entre generaciones V5/V6 y confirmar variante exacta para 3 mm.

### Electrónica
- Arquitectura de la era Arduino Mega / RAMPS o equivalente.
- Stepper drivers en módulos con disipadores.
- LCD RepRapDiscount / BigTreeTech Full Graphic Smart Controller 12864.
- Fuente metálica con borneros expuestos.

**Decisión Revival:** documentar la electrónica original, pero rediseñar alimentación, control, cableado, carcasas y seguridad con criterios actuales.

### Cama
- Cama calefactada con superficie de vidrio.
- Nivelación mediante tornillos y muelles.

### Transmisión X/Y
- Correas dentadas antiguas.
- Poleas y tensado a revisar.

## Próximos datos necesarios

1. Diámetro y longitud de varillas lisas X/Y/Z.
2. Diámetro y paso de las varillas roscadas actuales de Z.
3. Diámetro de las varillas estructurales Y.
4. Dimensiones del marco.
5. Etiquetas completas de todos los NEMA17.
6. Fotografía frontal/perpendicular de la placa controladora.
7. Etiqueta y especificaciones de la fuente.
8. Identificación exacta del hotend E3D.
9. Inventario de la caja de piezas y motores sueltos.
10. Estado de rodamientos lineales, poleas, correas y cama.

## Regla de seguridad

No alimentar la electrónica antigua hasta completar inspección visual, continuidad, estado del cableado, terminales, fuente, cama y protecciones.
