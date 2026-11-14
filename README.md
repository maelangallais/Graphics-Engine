# 📐 Graphics-Engine

A complete **2D rasterization and geometric drawing suite** built from scratch in MicroPython using **NumWorks' `kandinsky`** module — covering polygons, circles, triangles, and 8-connected line algorithms.

---

## 📂 Repository Structure

```
Graphics-Engine/
├── kandinsky_shapes.py              # All-in-one geometric shape library (100% set_pixel)
├── kandinsky_polygon_filler.py      # Experimental point-based polygon & circle scanline filler
├── circles/
│   ├── optimized_circle.py          # Optimized circle & disk rasterization functions
│   └── experiments/
│       ├── circle_trigo.py          # Early trigonometric circle experiment
│       ├── filled_circle.py         # Early filled disk experiment
│       ├── round_and_circle.py      # Combined circle & disk helper functions
│       └── circle_angled_arc.py     # Continuous single-loop circle with start angle & direction
├── triangles/
│   ├── triangle_from_sides.py       # Triangle drawer from 3 side lengths
│   └── triangle_trigo.py            # Two trigonometric triangle drawing approaches
└── draw_line/
    ├── draw_line.py                 # Adaptive line rasterizer with variable thickness & color
    └── draw_line_8_connected.py     # 8-connected 1px line rasterizer
```

---

## 🎨 Root Kandinsky Engines

### Multi-Shape Engine
[`kandinsky_shapes.py`](kandinsky_shapes.py) · *Created March 26, 2023*

A comprehensive shape-drawing library built **exclusively on `set_pixel`**, supporting:
- Rectangles (filled, outlined, and tilted left/right)
- Triangles (up, down, left, right)
- 3D-style parallelepipeds (left/right perspective)
- Filled disks and outlined circles

*(Note: Uses the original basic circle implementation rather than the later optimized versions in `circles/optimized_circle.py`.)*

### Polygon Scanline Filler *(Experimental)*
[`kandinsky_polygon_filler.py`](kandinsky_polygon_filler.py) · *Created November 11, 2026*

An experimental universal shape engine that draws and scanline-fills **arbitrary closed polygons** from any list of 3+ points (plus circles) using `set_pixel` and `get_pixel` parity ray-casting.
- **Known Limitations**: This is an early experimental prototype and is **very error-prone** — corners/vertices frequently cause scanline parity glitches (see the open enhancement issue), and setting pixel scale `t = 1` is very slow on hardware.

---

## ⭕ Circles (`circles/`)

### Optimized Circle *(Parent)*
[`circles/optimized_circle.py`](circles/optimized_circle.py) · *Created September 18, 2025*

Clean, optimized functions for drawing crisp circles and filled disks on the NumWorks screen. *(Functions written with AI assistance.)*

### Circle Experiments (`circles/experiments/`)
- [`circle_trigo.py`](circles/experiments/circle_trigo.py) · *Created September 13, 2023* — Initial trigonometric circle test (inefficient).
- [`filled_circle.py`](circles/experiments/filled_circle.py) · *Created September 13, 2023* — Early self-taught filled disk rasterizer.
- [`round_and_circle.py`](circles/experiments/round_and_circle.py) · *Created September 15, 2023* — Second experimental script bundling circle and disk helpers.
- [`circle_angled_arc.py`](circles/experiments/circle_angled_arc.py) · *Created October 20, 2026* — Continuous single-loop circle supporting custom starting angle (`ai`, e.g., `120°`) and drawing direction (`c = 0` for counter-clockwise, else clockwise).

---

## 🔺 Triangles (`triangles/`)

### Triangle from Side Lengths
[`triangles/triangle_from_sides.py`](triangles/triangle_from_sides.py) · *Created May 03, 2023*

Draws a triangle given the lengths of its 3 sides. Works reliably on general scalene triangles, though degenerate/very flat or equilateral edge cases can fail.

### Trigonometric Triangles
[`triangles/triangle_trigo.py`](triangles/triangle_trigo.py) · *Created February 22, 2023*

Early script testing two different trigonometric methods for drawing triangles.

---

## 📏 Line Rasterizers (`draw_line/`)

### Adaptive Line Drawer
[`draw_line/draw_line.py`](draw_line/draw_line.py) · *Created May 09, 2024*

Draws adaptive lines between any two points with configurable thickness (`span`) and color.

### 8-Connected Line Drawer
[`draw_line/draw_line_8_connected.py`](draw_line/draw_line_8_connected.py) · *Created October 22, 2026*

Refined line rasterizer ensuring strict **8-connectivity** (no diagonal pixel gaps) when drawing 1px-thick lines.

---

## 🖥️ Requirements & Platform

- MicroPython for **NumWorks** calculators (`kandinsky`, `math`).
