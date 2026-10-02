# Pathway Basecamp — Prompt Pack Gambar

Tema: **Jalur Pendakian**. Semua gambar ini dipakai untuk landing page parallax Pathway.
Simpan setiap hasil dengan **nama file persis seperti di judul prompt** (misalnya `L1-sky.png`), supaya bisa langsung dirakit ke kode.

---

## 0. Aturan main (baca dulu)

1. **Generate `M0-master.png` paling pertama.** Ini gambar acuan komposisi. Semua gambar berikutnya di-generate dengan melampirkan M0 sebagai referensi.
2. **Cahaya hanya dari satu arah:** matahari terbit di **kiri-tengah horizon**, cahaya hangat datang dari kiri. Jangan sampai ada gambar yang disinari dari kanan.
3. **Ukuran:**
   - Lapisan adegan utama (L1–L8): **21:9, minimal 2560 px lebar** (lebih besar lebih baik, 3840 px ideal).
   - Close-up tujuan (C): **16:9, minimal 2560 px lebar**.
   - Aset kecil (P, F, I): **1:1, minimal 1024 px**.
4. **Latar transparan (PNG)** untuk semua kecuali L1, M0, dan lapisan "bg" close-up. Kalau tool-mu tidak bisa transparan, pakai **hijau polos #00FF00**. Pinggirannya nanti kubersihkan.
5. **Tanpa teks sama sekali.** Papan kayu, plakat, dan patok harus kosong. Tulisan dipasang lewat kode.
6. **Bagian bawah setiap lapisan diisi penuh sampai tepi**, jangan terpotong atau memudar ke transparan di bawah (kecuali disebut), supaya tidak ada celah saat lapisan bergeser.

### Blok gaya (tempel di AKHIR setiap prompt)

```text
Style: painterly layered paper-cut illustration, textured handmade paper grain, soft shadows between paper layers, warm sunrise light coming from the left-center horizon, palette of deep indigo, violet, warm orange and golden yellow, pine greens and earthy browns. Same style, palette and lighting as the reference image. No text, no letters, no numbers, no logos, no watermark, no 3D render, no glossy plastic.
```

Di bawah, blok ini ditulis sebagai **[STYLE]**.

---

## M. Acuan komposisi

### M0-master.png (opaque, 21:9)

```text
Wide panoramic illustration, 21:9, at least 2560 px wide. A mountain hiking scene at sunrise seen from a basecamp. Gradient sky from deep indigo at the top to warm orange at the horizon, sun rising at the left-center horizon. Layered distant violet mountain ranges with morning mist, a calm lake in the left-center valley reflecting the sunrise. A tall rocky main mountain in the right third with a small red flag on its summit. Green rolling hills in the midground with pine forests, and a winding dirt hiking trail with small wooden trail posts climbing from the bottom center to the summit. Foreground: on the left a wooden trail signpost with four blank arrow boards, an orange tent, a backpack and rocks; tall pine trees framing the left and right edges; tall grass along the bottom. Keep the upper-left sky calm and open for a headline.
[STYLE]
```

---

## L. Lapisan adegan utama (urutan dari paling jauh ke paling dekat)

### L1-sky.png (opaque, 21:9)

```text
Sky only, 21:9, at least 2560 px wide. Smooth gradient from deep indigo at the top through violet to warm orange and golden yellow at the bottom horizon. A glowing sun half-risen at the left-center bottom edge, with a soft warm halo. No clouds, no mountains, no land, no trees, nothing else.
[STYLE]
```

### L2a-clouds-far.png (transparent, 21:9)

```text
Only thin, wispy high-altitude clouds scattered across the upper half of the frame, lit pink and gold from below by the sunrise on the left. Isolated on a transparent background. No sky color, no sun, no mountains, no land.
[STYLE]
```

### L2b-clouds-near.png (transparent, 21:9)

```text
Only three or four larger, puffy paper-cut clouds with warm golden-pink edges, placed in the upper right and upper middle, leaving the upper-left area empty. Isolated on a transparent background. No sky color, no sun, no mountains, no land.
[STYLE]
```

### L3-far-ranges.png (transparent top, 21:9)

```text
Only the distant layered mountain ranges in soft violet and blue-grey tones with bands of morning mist between them, and a calm lake in the left-center valley reflecting the orange sunrise. The ranges sit in the lower half of the frame. Everything above the mountain ridgelines is transparent. The lake and lowland continue fully to the bottom edge. No sky, no sun, no clouds, no main tall mountain, no trees in front.
[STYLE]
```

### L4-main-mountain.png (transparent, 21:9)

```text
Only one tall rocky main mountain in the right third of the frame, with snowy ridges catching warm light on the left side and cool violet shadows on the right side. The summit is bare with NO flag. Its base widens and continues fully to the bottom edge. Everything else is transparent. No sky, no other mountains, no lake, no hills, no trail.
[STYLE]
```

### L5-midground-trail.png (transparent top, 21:9)

```text
Only the midground: green rolling hills with scattered pine forests across the full width, and a winding dirt hiking trail with small blank wooden trail posts that starts at the bottom center and climbs toward the upper right, ending where the main mountain would begin. Hills fill the lower 55 percent of the frame and continue fully to the bottom edge. Everything above the hill line is transparent. No sky, no distant mountains, no main mountain, no lake.
[STYLE]
```

### L6-mist.png (transparent, 21:9)

```text
Only soft horizontal bands of white morning mist and low fog, semi-transparent and feathered, floating in two or three layers across the middle and lower-middle of the frame. Isolated on a transparent background. No landscape, no sky color, no objects.
[STYLE]
```

### L7-foreground.png (transparent, 16:9)

```text
Foreground frame layer, 16:9, at least 2560 px wide. Left side: an orange camping tent, a dark green hiking backpack with a rolled sleeping mat, large grey rocks. Left and right edges: tall dark green pine trees partially cut off by the frame. Bottom edge: tall wild grass, small white wildflowers and rocks along the full width, with a dirt patch at the bottom center where the trail begins. NO signpost. The center and upper area of the image are completely empty and transparent.
[STYLE]
```

### L8-near-blur.png (transparent, 16:9)

```text
Extreme close foreground: a few large out-of-focus grass blades and pine needles entering from the bottom-left and bottom-right corners, softly blurred like a shallow depth of field camera lens, warm backlight from the left. Everything else is transparent. No landscape, no objects.
[STYLE]
```

---

## P. Papan penunjuk jalan (dipisah supaya bisa beranimasi "terlipat keluar")

Semua 1:1, transparan, kayu yang sama. Generate P0 dulu, lalu lampirkan P0 sebagai referensi untuk P1–P4.

### P0-signpost-pole.png

```text
Only a single vertical weathered wooden signpost pole with a few small metal nail heads and wood grain, standing upright, slightly rough round top. No boards attached. Isolated on a transparent background.
[STYLE]
```

### P1-board-left-long.png

```text
Only one long blank wooden arrow board pointing LEFT, flat front view, weathered wood grain, two small nail heads near the right end. Isolated on a transparent background. No text, no pole.
[STYLE]
```

### P2-board-right-long.png

```text
Only one long blank wooden arrow board pointing RIGHT, flat front view, weathered wood grain, two small nail heads near the left end. Isolated on a transparent background. No text, no pole.
[STYLE]
```

### P3-board-left-short.png

```text
Only one short blank wooden arrow board pointing LEFT, flat front view, slightly darker weathered wood, two small nail heads near the right end. Isolated on a transparent background. No text, no pole.
[STYLE]
```

### P4-board-up.png

```text
Only one blank wooden arrow board pointing diagonally UP and to the right, toward a summit, flat front view, weathered wood grain with a small orange painted stripe near the arrow tip. Isolated on a transparent background. No text, no pole.
[STYLE]
```

---

## F. Aset kecil yang bergerak

### F1-flag.png (1:1, transparan)

```text
Only a small red cloth flag on a thin wooden pole, flag gently waving to the right, lit by warm morning light from the left. Isolated on a transparent background. No mountain, no ground.
[STYLE]
```

### F2-birds.png (transparan, 16:9)

```text
Only a small loose flock of seven distant birds in flight, simple dark silhouettes with slightly different wing positions, spread across the frame. Isolated on a transparent background.
[STYLE]
```

### F3-campfire.png (1:1, transparan)

```text
Only a small campfire: a ring of stones, crossed logs and bright warm orange and yellow flames with a few floating sparks. Isolated on a transparent background.
[STYLE]
```

### F4-lantern.png (1:1, transparan)

```text
Only an old metal camping lantern with a warm glowing flame inside, hanging from a short hook. Isolated on a transparent background.
[STYLE]
```

---

## C. Close-up tujuan (muncul di akhir perjalanan kamera)

Setiap tujuan = 2 gambar: **bg** (opaque) dan **fg** (transparan). Lampirkan M0 sebagai referensi supaya tempatnya terasa satu dunia.

### C1 — Tentang (tepi hutan basecamp)

**C1-tentang-bg.png** (opaque, 16:9)

```text
Close-up view at the edge of a misty pine forest near a mountain basecamp at sunrise, warm light rays streaming through the trees from the left, soft mist on the ground, glimpses of violet mountains through the trees.
[STYLE]
```

**C1-tentang-fg.png** (transparan, 16:9)

```text
Only foreground objects on the right half: a blank wooden information board on two posts with a small roof, a log bench in front of it, and ferns and grass at the bottom edge. The left half and the upper area are completely transparent. No text on the board.
[STYLE]
```

### C2 — Cara Kerja (jalur menanjak)

**C2-cara-bg.png** (opaque, 16:9)

```text
Close-up of a winding dirt hiking trail climbing a green grassy ridge toward a tall snowy summit with a tiny red flag in the far distance, small wooden trail posts along the trail, golden morning light from the left, mist in the valleys below.
[STYLE]
```

**C2-cara-fg.png** (transparan, 16:9)

```text
Only foreground objects: on the left a large wooden trail post with a blank metal plate, a hiking backpack and trekking pole leaning against it; tall grass and rocks along the bottom edge. The center, right and upper area are completely transparent. No text on the plate.
[STYLE]
```

### C3 — Komunitas (api unggun di tepi danau)

**C3-komunitas-bg.png** (opaque, 16:9)

```text
Close-up of a calm mountain lake shore at dawn, the lake reflecting the orange sunrise, violet mountains and morning mist on the far side, a few pine trees on the shore.
[STYLE]
```

**C3-komunitas-fg.png** (transparan, 16:9)

```text
Only foreground: a group of six young hikers seen as warm-lit silhouettes from behind and the side, sitting together on logs in a loose circle, some laughing and talking, backpacks beside them; an empty space in the middle of the circle for a campfire; grass at the bottom edge. Everything else is transparent.
[STYLE]
```

### C4 — Puncak

**C4-puncak-bg.png** (opaque, 16:9)

```text
View from a mountain summit at full morning light: a sea of soft clouds below, distant violet peaks poking through, bright golden sky with the sun higher above the horizon on the left.
[STYLE]
```

**C4-puncak-fg.png** (transparan, 16:9)

```text
Only foreground: the rocky summit top in the lower center and lower right, a short wooden pole for a flag with NO flag on it, a small blank wooden plaque fixed to a rock, and a hiker silhouette standing with arms raised on the left side of the summit. Everything above the rocks is transparent. No text on the plaque.
[STYLE]
```

---

## I. Ikon "Empat pos" untuk bagian bawah halaman

Semua 1:1, transparan, ukuran sama, komposisi di tengah.

### I1-basecamp.png

```text
Small spot illustration centered: an orange tent with a tiny pine tree beside it on a round patch of grass. Isolated on a transparent background.
[STYLE]
```

### I2-pos1.png

```text
Small spot illustration centered: a blank wooden trail post with a hiking backpack leaning on it, on a round patch of dirt trail. Isolated on a transparent background.
[STYLE]
```

### I3-pos2.png

```text
Small spot illustration centered: an open journal notebook and a pencil next to a small campfire on a round patch of grass. Isolated on a transparent background. No writing on the pages.
[STYLE]
```

### I4-puncak.png

```text
Small spot illustration centered: a small rocky summit with a red flag on top and a tiny sun behind it. Isolated on a transparent background.
[STYLE]
```

---

## X. Opsional

### X1-paper-texture.png (1:1, opaque)

```text
Seamless tileable texture of warm cream handmade paper with subtle fibers and grain, very low contrast, flat even lighting, top-down. No objects, no shadows, no text.
```

### X2-foreground-mobile.png (transparan, 9:16)

```text
Vertical 9:16 foreground frame for a phone screen. Bottom third only: an orange tent and a backpack in the bottom-left, rocks and tall grass along the full bottom edge, one pine tree partly cut off at the right edge. The upper two thirds are completely transparent. NO signpost.
[STYLE]
```

---

## Urutan generate yang disarankan

| Tahap | File | Untuk apa |
|---|---|---|
| 1 | M0 | Acuan komposisi dan cahaya |
| 2 | L1, L3, L4, L5, L7 | Parallax inti 5 lapis |
| 3 | P0–P4, F1 | Papan yang terlipat keluar + bendera berkibar |
| 4 | L2a, L2b, L6, L8, F2 | Awan, kabut, blur dekat, burung (gerak ambient) |
| 5 | C1–C4 (bg + fg), F3, F4 | Close-up tujuan kamera |
| 6 | I1–I4, X1, X2 | Bagian bawah halaman dan versi HP |

Tahap 1–3 sudah cukup untuk lompatan besar. Kirim hasilnya per tahap, nanti kurakit bertahap.
