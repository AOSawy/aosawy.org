# Portfolio Showcase Design System — Apple Liquid Glass

> **Purpose:** Canonical reference for building all engineering project showcases.
> Every new showcase MUST follow these exact tokens, components, and patterns.
> **Last audited:** 2026-03-29 across all 7 AUC showcases.

---

## 1. COLOR PALETTE

All 7 showcases use an identical 9-color system. Never deviate.

```js
const color = {
  bg:           '#f5f5f7',              // Page background (Apple light grey)
  text:         '#1d1d1f',              // Primary text
  secondary:    '#6e6e73',              // Secondary text
  tertiary:     '#86868b',              // Tertiary text, captions, labels
  accent:       '#0071e3',              // Primary accent (Apple blue)
  accentLight:  'rgba(0,113,227,0.06)', // Accent tint for backgrounds
  accentBorder: 'rgba(0,113,227,0.15)', // Accent tint for borders
  border:       'rgba(0,0,0,0.06)',     // Default subtle border
  white:        '#ffffff',              // Pure white
};
```

---

## 2. GLASSMORPHISM TOKENS

Three-tier glass system. Always include both `backdropFilter` AND `WebkitBackdropFilter`.

```js
const glass = {
  card: {
    background:          'rgba(255,255,255,0.65)',
    backdropFilter:      'saturate(180%) blur(20px)',
    WebkitBackdropFilter:'saturate(180%) blur(20px)',
    border:              `0.5px solid rgba(0,0,0,0.06)`,
    borderRadius:        '16px',
    boxShadow:           '0 1px 4px rgba(0,0,0,0.03)',
  },
  // Hover state for cards (applied via onMouseEnter/onMouseLeave):
  cardHover: {
    boxShadow:  '0 4px 20px rgba(0,0,0,0.06)',
    transform:  'translateY(-2px)',
  },
  nav: {
    background:          'rgba(255,255,255,0.72)',
    backdropFilter:      'saturate(180%) blur(20px)',
    WebkitBackdropFilter:'saturate(180%) blur(20px)',
    borderBottom:        `0.5px solid rgba(0,0,0,0.06)`,
  },
  surface: {
    background:          'rgba(255,255,255,0.45)',
    backdropFilter:      'saturate(120%) blur(12px)',
    WebkitBackdropFilter:'saturate(120%) blur(12px)',
    border:              `0.5px solid rgba(0,0,0,0.04)`,
    borderRadius:        '14px',
  },
};
```

---

## 3. TYPOGRAPHY

### Font Families

| Role | Stack |
|------|-------|
| **Headings** | `'Playfair Display', Georgia, serif` |
| **Body / UI** | `'Inter', -apple-system, sans-serif` |
| **Monospace / Code / Data** | `'SF Mono', 'Fira Code', 'Consolas', monospace` |
| **Math / Equations** | `'Cambria Math', 'Latin Modern Math', 'STIX Two Math', 'Georgia', 'Times New Roman', serif` |

### Type Scale

| Element | fontSize | fontWeight | letterSpacing | lineHeight | fontFamily |
|---------|----------|------------|---------------|------------|------------|
| Hero H1 | `2.2rem` | 700 | `-0.02em` | — | Playfair Display |
| SectionTitle | `1.5rem` | 600 | `-0.01em` | — | Playfair Display |
| StatCard value | `1.7rem` | 700 | `-0.02em` | — | Inter |
| StatCard label | `0.72rem` | 600 | `1.5px` | — | Inter (uppercase) |
| StatCard sub | `0.75rem` | 400 | — | — | Inter |
| StatCard unit | `0.9rem` | 500 | — | — | Inter |
| Body text | `0.92rem` | 400 | — | 1.8 | Inter |
| Pill button | `0.82rem` | 500 | — | — | Inter |
| Hero badge | `0.7rem` | 600 | `2px` | — | Inter (uppercase) |
| Hero subtitle | `0.92rem` | 400 | — | 1.65 | Inter |
| Table header | `0.75rem` | 600 | `1px` | — | Inter (uppercase) |
| Table body | `0.82rem` | 400 | — | — | Inter |
| Doc link | `0.85rem` | 500 | — | — | Inter |
| Image caption | `0.78rem` | 400 | — | 1.4 | Inter |
| Footer main | `0.75rem` | 400 | — | — | Inter |
| Footer sub | `0.7rem` | 400 | — | — | Inter (opacity 0.7) |
| Code block | `0.72rem` | 400 | — | 1.7 | SF Mono |
| Equation display | `1.15rem` | 400 | `0.5px` | — | Cambria Math |
| Equation inline | `1rem` | 400 | `0.3px` | — | Cambria Math |

---

## 4. BORDER-RADIUS SCALE

| Value | Usage |
|-------|-------|
| `980px` | Pill buttons, hero badge (fully rounded) |
| `50%` | Circular badges (step numbers) |
| `20px` | Hero card |
| `16px` | GlassCard (standard cards) |
| `14px` | Glass.surface, floating stats |
| `12px` | Chart tooltips |
| `10px` | Scroll indicator outer, equation lines |
| `8px` | Chart bar tops `[8, 8, 0, 0]` |
| `4px` | Small elements |

---

## 5. SPACING SYSTEM

### Main Layout

```js
// Main content wrapper — IDENTICAL across all 7 showcases
<main style={{ maxWidth: '1200px', margin: '0 auto', padding: '3rem 2rem 4rem' }}>
```

### Section Spacing

| Context | Value |
|---------|-------|
| Gap between major sections (tab content) | `2.5rem` |
| SectionTitle marginBottom | `1.25rem` |
| Grid gap (standard) | `1.25rem` |
| Grid gap (tight) | `1rem` |
| Grid gap (wide) | `1.5rem` |
| Nav pill gap | `0.5rem` |
| Hero content gap | `1.5rem` |
| Floating stats gap | `1rem` |

### Component Padding

| Component | Padding |
|-----------|---------|
| StatCard | `1.25rem 1.5rem` |
| EquationBlock | `1.75rem 2rem` |
| StepCard | `1.5rem` |
| DataTable header cell | `12px 16px` |
| DataTable body cell | `10px 16px` |
| Table caption | `0.75rem 1rem` |
| Hero card | `2rem` |
| Hero badge | `8px 20px` |
| Nav bar | `12px 0` |
| Nav container horizontal | `0 2rem` |
| Code block header | `12px 20px` |
| Code block body | `1.5rem 1.75rem` |
| Footer | `2rem` |
| Document link | `12px 20px` |

---

## 6. SHADOW SYSTEM

| Level | Value | Usage |
|-------|-------|-------|
| Resting | `0 1px 4px rgba(0,0,0,0.03)` | GlassCard default |
| Hover | `0 4px 20px rgba(0,0,0,0.06)` | GlassCard hover |
| Chart tooltip | `0 4px 16px rgba(0,0,0,0.08)` | Recharts tooltip |
| Hero card | `0 8px 32px rgba(0,0,0,0.2)` | Hero content card |

---

## 7. ANIMATIONS & TRANSITIONS

### Keyframes

```css
@keyframes heroFloat {
  0%, 100% { transform: translateX(-50%) translateY(0); }
  50%      { transform: translateX(-50%) translateY(6px); }
}
```

Used on the scroll indicator: `animation: heroFloat 2s ease-in-out infinite`

### Transition Durations

| Duration | Easing | Usage |
|----------|--------|-------|
| `0.25s` | ease | GlassCard hover (all properties) |
| `0.2s` | ease | Pill buttons, document links, nav items |
| `0.2s` | ease | LinkedIn link opacity |

---

## 8. HERO SECTION

### Container
```js
{
  position: 'relative',
  height: '100vh',       // CANONICAL — see inconsistencies note
  overflow: 'hidden',
  fontFamily: "'Inter', -apple-system, sans-serif",
}
```

### Background Media
- Video: `position: absolute`, `top: 0, left: 0`, `width/height: 100%`, `objectFit: 'cover'`, `zIndex: 0`
- Autoplay, muted, loop, playsInline

### Gradient Overlay
```js
{
  position: 'absolute', top: 0, left: 0, right: 0, bottom: 0,
  background: 'linear-gradient(180deg, rgba(0,0,0,0.4) 0%, transparent 35%, transparent 55%, rgba(0,0,0,0.6) 100%)',
  zIndex: 1,
}
```

### Content Card
```js
// Container
{ position: 'absolute', bottom: '12%', left: '5%', zIndex: 5,
  maxWidth: '600px', textAlign: 'left',
  display: 'flex', flexDirection: 'column', gap: '1.5rem' }

// Card itself
{ background: 'rgba(255,255,255,0.06)',
  backdropFilter: 'blur(24px)', WebkitBackdropFilter: 'blur(24px)',
  border: '0.5px solid rgba(255,255,255,0.1)',
  borderRadius: '20px', padding: '2rem',
  boxShadow: '0 8px 32px rgba(0,0,0,0.2)' }
```

### Hero Text

```js
// Badge (course code)
{ display: 'inline-block', padding: '8px 20px', borderRadius: '980px',
  background: 'rgba(255,255,255,0.1)',
  border: '0.5px solid rgba(255,255,255,0.15)',
  color: 'rgba(255,255,255,0.9)', fontSize: '0.7rem',
  fontWeight: 600, letterSpacing: '2px', textTransform: 'uppercase' }

// H1
{ fontSize: '2.2rem', fontWeight: 700,
  fontFamily: "'Playfair Display', Georgia, serif",
  letterSpacing: '-0.02em', color: '#ffffff',
  margin: '0 0 1rem 0', lineHeight: 1.15 }

// Subtitle / description
{ fontSize: '0.92rem', color: 'rgba(255,255,255,0.8)',
  lineHeight: 1.65, margin: '0 0 1.25rem 0', maxWidth: '520px' }

// Instructor links (LinkedIn)
{ color: 'rgba(255,255,255,0.95)', textDecoration: 'none',
  fontWeight: 500, opacity: 0.9 }
// hover: opacity 0.6, transition: 'opacity 0.2s ease'
```

### Floating Stats (top-right)
```js
// Container
{ position: 'absolute', top: '5%', right: '5%', zIndex: 5,
  display: 'flex', gap: '1rem' }

// Each stat chip
{ background: 'rgba(255,255,255,0.06)',
  backdropFilter: 'blur(16px)', WebkitBackdropFilter: 'blur(16px)',
  border: '0.5px solid rgba(255,255,255,0.08)',
  borderRadius: '14px', padding: '1rem 1.25rem' }

// Stat value
{ fontSize: '1.2rem', fontWeight: 700, color: '#ffffff',
  letterSpacing: '-0.02em' }

// Stat label
{ fontSize: '0.65rem', color: 'rgba(255,255,255,0.6)',
  textTransform: 'uppercase', letterSpacing: '1.5px',
  fontWeight: 500, marginTop: '4px' }
```

### Scroll Indicator (bottom-center)
```js
// Wrapper
{ position: 'absolute', bottom: '4%', left: '50%',
  transform: 'translateX(-50%)', zIndex: 10,
  display: 'flex', flexDirection: 'column', alignItems: 'center',
  gap: '6px', opacity: 0.4,
  animation: 'heroFloat 2s ease-in-out infinite' }

// Outer pill
{ width: '20px', height: '32px', borderRadius: '10px',
  border: '1.5px solid rgba(255,255,255,0.4)',
  display: 'flex', justifyContent: 'center', paddingTop: '6px' }

// Inner dot
{ width: '2px', height: '8px', borderRadius: '1px',
  background: 'rgba(255,255,255,0.6)' }

// "Scroll" label
{ fontSize: '0.55rem', letterSpacing: '2px',
  textTransform: 'uppercase', color: 'rgba(255,255,255,0.4)',
  fontWeight: 500 }
```

### Hero Document Links (PDFs in hero)
```js
// Link container
{ display: 'flex', gap: '12px', flexWrap: 'wrap', marginTop: '0.5rem' }

// Each link
{ display: 'inline-flex', alignItems: 'center', gap: '8px',
  padding: '8px 16px', borderRadius: '8px',
  background: 'rgba(255,255,255,0.1)',
  border: '0.5px solid rgba(255,255,255,0.15)',
  color: '#ffffff', textDecoration: 'none',
  fontSize: '0.78rem', fontWeight: 500,
  transition: 'all 0.2s ease' }
// hover: background → 'rgba(0,113,227,0.2)'
```

---

## 9. NAVIGATION / TAB BAR

```js
// Nav bar container
{ ...glass.nav, position: 'sticky', top: 0, zIndex: 50, padding: '12px 0' }

// Nav inner (centers pills)
{ maxWidth: '1200px', margin: '0 auto',
  display: 'flex', gap: '0.5rem',
  justifyContent: 'center', flexWrap: 'wrap',
  padding: '0 2rem' }
```

### Pill Component
```js
// Base style
{ padding: '8px 20px', borderRadius: '980px',
  fontSize: '0.82rem', fontWeight: 500,
  cursor: 'pointer', transition: 'all 0.2s ease' }

// Active state
{ background: color.accent, color: '#fff', border: 'none' }

// Inactive state
{ background: 'transparent', color: color.accent,
  border: `0.5px solid ${color.accentBorder}` }
```

### Tab Count Convention
- Standard: **5 tabs** (6 of 7 showcases)
- Exception: Thesis has 6 tabs (Overview, Design, Economics, Results, Safety, Future Work)

---

## 10. REUSABLE COMPONENTS

### GlassCard
```jsx
function GlassCard({ children, style = {}, hover = true }) {
  const [isHovered, setIsHovered] = useState(false);
  return (
    <div
      onMouseEnter={() => hover && setIsHovered(true)}
      onMouseLeave={() => hover && setIsHovered(false)}
      style={{
        ...glass.card,
        transition: 'all 0.25s ease',
        ...(isHovered ? glass.cardHover : {}),
        ...style,
      }}
    >
      {children}
    </div>
  );
}
```

### SectionTitle
```jsx
function SectionTitle({ children }) {
  return (
    <h2 style={{
      fontSize: '1.5rem', fontWeight: 600,
      fontFamily: "'Playfair Display', Georgia, serif",
      color: color.text, letterSpacing: '-0.01em',
      marginBottom: '1.25rem',
    }}>
      {children}
    </h2>
  );
}
```

### StatCard (Standard — with unit/sub)
```jsx
function StatCard({ label, value, unit, sub }) {
  return (
    <GlassCard style={{ padding: '1.25rem 1.5rem', flex: '1 1 180px', minWidth: 160 }}>
      <div style={{ fontSize: '0.72rem', color: color.tertiary,
        textTransform: 'uppercase', letterSpacing: '1.5px',
        fontWeight: 600, marginBottom: '0.5rem' }}>
        {label}
      </div>
      <div style={{ fontSize: '1.7rem', fontWeight: 700,
        color: color.text, letterSpacing: '-0.02em' }}>
        {value}
        <span style={{ fontSize: '0.9rem', color: color.secondary,
          fontWeight: 500, marginLeft: '4px' }}>{unit}</span>
      </div>
      {sub && <div style={{ fontSize: '0.75rem', color: color.tertiary,
        marginTop: '4px' }}>{sub}</div>}
    </GlassCard>
  );
}
```

### ImageCard
```jsx
function ImageCard({ src, alt, caption, aspect = 1.5 }) {
  return (
    <GlassCard style={{ overflow: 'hidden', padding: 0 }}>
      <div style={{ position: 'relative',
        paddingBottom: `${(1 / aspect) * 100}%` }}>
        <img src={src} alt={alt || caption || ''}
          loading="lazy"
          style={{ position: 'absolute', top: 0, left: 0,
            width: '100%', height: '100%',
            objectFit: 'contain',  // use 'cover' for photos
            background: '#ffffff', // white bg for technical drawings
          }}
        />
      </div>
      {caption && (
        <div style={{ padding: '0.75rem 1rem',
          fontSize: '0.78rem', color: color.secondary,
          lineHeight: 1.4 }}>
          {caption}
        </div>
      )}
    </GlassCard>
  );
}
```

**objectFit rules:**
- Photos/renders → `cover`
- Technical drawings, charts, diagrams → `contain` (with white or `#f0f0f2` background)

### DataTable
```jsx
function DataTable({ columns, data, mono = [], caption }) {
  return (
    <GlassCard style={{ overflow: 'hidden', padding: 0 }}>
      <div style={{ overflowX: 'auto' }}>
        <table style={{ width: '100%', borderCollapse: 'collapse',
          fontSize: '0.82rem', fontFamily: "'Inter', -apple-system, sans-serif" }}>
          <thead>
            <tr style={{ background: color.accentLight }}>
              {columns.map((col, i) => (
                <th key={i} style={{ padding: '12px 16px', textAlign: 'left',
                  fontWeight: 600, color: color.text,
                  borderBottom: `1px solid ${color.border}`,
                  whiteSpace: 'nowrap',
                  fontSize: '0.75rem', textTransform: 'uppercase',
                  letterSpacing: '1px' }}>
                  {col}
                </th>
              ))}
            </tr>
          </thead>
          <tbody>
            {data.map((row, i) => (
              <tr key={i} style={{ borderBottom: `0.5px solid ${color.border}` }}>
                {row.map((cell, j) => (
                  <td key={j} style={{
                    padding: '10px 16px',
                    color: j === 0 ? color.text : color.secondary,
                    fontWeight: j === 0 ? 500 : 400,
                    fontFamily: mono.includes(j)
                      ? "'SF Mono', 'Fira Code', monospace" : 'inherit',
                    fontVariantNumeric: mono.includes(j) ? 'tabular-nums' : 'normal',
                  }}>
                    {cell}
                  </td>
                ))}
              </tr>
            ))}
          </tbody>
          {caption && (
            <caption style={{ captionSide: 'bottom', padding: '0.75rem 1rem',
              fontSize: '0.72rem', color: color.tertiary,
              borderTop: `0.5px solid ${color.border}` }}>
              {caption}
            </caption>
          )}
        </table>
      </div>
    </GlassCard>
  );
}
```

### StepCard
```jsx
function StepCard({ number, name, desc }) {
  return (
    <GlassCard style={{ padding: '1.5rem', textAlign: 'center', position: 'relative' }}>
      <div style={{ position: 'absolute', top: '-12px', left: '50%',
        transform: 'translateX(-50%)',
        width: '32px', height: '32px',
        background: color.accent, color: '#ffffff',
        borderRadius: '50%', fontWeight: 700, fontSize: '0.9rem',
        display: 'flex', alignItems: 'center', justifyContent: 'center',
        boxShadow: '0 2px 8px rgba(0,113,227,0.3)' }}>
        {number}
      </div>
      <div style={{ fontWeight: 600, color: color.text,
        marginTop: '12px', marginBottom: '0.5rem', fontSize: '0.95rem' }}>
        {name}
      </div>
      <div style={{ fontSize: '0.82rem', color: color.secondary, lineHeight: 1.6 }}>
        {desc}
      </div>
    </GlassCard>
  );
}
```

### Document Links (in-page, post-hero)
```jsx
// Container
<div style={{ display: 'flex', gap: '12px', flexWrap: 'wrap' }}>

// Each link
<a href={url} target="_blank" rel="noopener noreferrer"
  style={{
    ...glass.card,
    display: 'inline-flex', alignItems: 'center', gap: '10px',
    padding: '12px 20px', textDecoration: 'none',
    color: color.accent, fontSize: '0.85rem', fontWeight: 500,
    transition: 'all 0.2s ease',
  }}
  onMouseEnter={e => { e.currentTarget.style.transform = 'translateY(-2px)';
    e.currentTarget.style.boxShadow = '0 4px 20px rgba(0,0,0,0.06)'; }}
  onMouseLeave={e => { e.currentTarget.style.transform = 'translateY(0)';
    e.currentTarget.style.boxShadow = glass.card.boxShadow; }}
>
  {/* PDF SVG icon */} {label}
</a>
```

---

## 11. RECHARTS CONFIGURATION

### Tooltip (glassmorphic)
```js
const tooltipStyle = {
  contentStyle: {
    background: 'rgba(255,255,255,0.85)',
    backdropFilter: 'blur(20px)',
    WebkitBackdropFilter: 'blur(20px)',
    border: `0.5px solid ${color.border}`,
    borderRadius: '12px',
    boxShadow: '0 4px 16px rgba(0,0,0,0.08)',
    fontFamily: "'Inter', -apple-system, sans-serif",
    fontSize: '0.8rem',
  },
  labelStyle: { color: color.text, fontWeight: 600 },
};
```

### Axes
```jsx
<XAxis dataKey="name" tick={{ fontSize: 12, fill: color.secondary }} />
<YAxis tick={{ fontSize: 12, fill: color.secondary }} />
<CartesianGrid strokeDasharray="3 3" stroke={color.border} />
```

### Bar Charts
```jsx
<Bar dataKey="value" fill={color.accent} radius={[8, 8, 0, 0]} />
```

### Line Charts
```jsx
<Line type="monotone" dataKey="value" stroke={color.accent}
  strokeWidth={2} dot={false} />
```

### ResponsiveContainer
```jsx
<ResponsiveContainer width="100%" height={350}>
```

---

## 12. THREE.JS 3D MODEL VIEWER

Used in: thesis, design-ii, am (with lazy CDN loading)

### Scene Setup
```js
scene.background = new THREE.Color(0xf5f5f7);  // matches page bg
renderer.outputColorSpace = THREE.SRGBColorSpace;
renderer.toneMapping = THREE.ACESFilmicToneMapping;
renderer.shadowMap.type = THREE.PCFSoftShadowMap;
```

### Camera
```js
camera = new THREE.PerspectiveCamera(40, width/height, 0.1, 1000);
```

### Lighting (4-light setup)
```js
// Ambient
new THREE.AmbientLight(0xffffff, 0.6)

// Main directional (with shadows)
directionalLight.position.set(5, 5, 3)  // ~45°, -45°, 30°
directionalLight.intensity = 1.4
directionalLight.castShadow = true
directionalLight.shadow.mapSize = 2048 x 2048

// Fill light
new THREE.DirectionalLight(0xb0c4de, 0.5)  // soft blue fill

// Rim light
new THREE.DirectionalLight(0xffffff, 0.3)   // from behind
```

### Ground Plane
```js
new THREE.PlaneGeometry(1000, 1000)
material.color = 0xeaeaed
receiveShadow = true
rotation.x = -Math.PI / 2
```

### OrbitControls
```js
controls.enableDamping = true
controls.dampingFactor = 0.05
controls.enablePan = false
controls.minDistance = 2
controls.maxDistance = 10
controls.autoRotate = true
controls.autoRotateSpeed = 1
```

### Loading Spinner
```js
// CSS animation: spin 1s linear infinite
{ width: '32px', height: '32px',
  border: '3px solid rgba(0,113,227,0.2)',
  borderTop: `3px solid ${color.accent}`,
  borderRadius: '50%',
  animation: 'spin 1s linear infinite' }
```

---

## 13. CODE BLOCK (dark theme)

Used in FEM for MATLAB/Python code displays.

```js
// Header bar
{ background: 'linear-gradient(135deg, #1e1e2e 0%, #2d2d3f 100%)',
  padding: '12px 20px',
  borderBottom: '1px solid rgba(255,255,255,0.06)' }

// Filename
{ fontSize: '0.78rem', fontWeight: 600, color: '#e0e0e0',
  letterSpacing: '0.5px' }

// Code body
{ margin: 0, padding: '1.5rem 1.75rem',
  background: '#1e1e2e', color: '#d4d4d4',
  fontSize: '0.72rem', lineHeight: 1.7,
  fontFamily: "'SF Mono', 'Fira Code', 'Consolas', monospace",
  maxHeight: '600px', overflowX: 'auto', overflowY: 'auto' }
```

---

## 14. EQUATION DISPLAY

Used in FEM, system-dynamics for mathematical notation.

### EquationBlock
```js
// Wrapper — GlassCard with extra padding
{ padding: '1.75rem 2rem' }

// Title
{ fontSize: '0.9rem', fontWeight: 600, marginBottom: '1.25rem' }

// Note (optional italic footer)
{ fontSize: '0.78rem', color: color.tertiary, marginTop: '1rem',
  fontStyle: 'italic', lineHeight: 1.5 }
```

### EquationLine
```js
// Container
{ display: 'flex', alignItems: 'center', gap: '1rem',
  padding: '0.75rem 1.25rem',
  background: numbered ? color.accentLight : 'transparent',
  borderRadius: '10px',
  borderLeft: numbered ? `3px solid ${color.accent}` : 'none',
  marginBottom: '0.5rem' }

// Equation text
{ fontFamily: mathFont, fontSize: '1.05rem',
  letterSpacing: '0.3px', lineHeight: 1.8 }

// Equation number
{ fontSize: '0.75rem', color: color.accent, fontWeight: 600,
  whiteSpace: 'nowrap' }
```

---

## 15. FOOTER

Identical across all 7 showcases.

```jsx
<footer style={{
  borderTop: `0.5px solid ${color.border}`,
  padding: '2rem',
  textAlign: 'center',
}}>
  <p style={{ fontSize: '0.75rem', color: color.tertiary, margin: 0 }}>
    {PROJECT_META.course} · {PROJECT_META.student} · {PROJECT_META.institution}
  </p>
  <p style={{ fontSize: '0.7rem', color: color.tertiary,
    margin: '8px 0 0 0', opacity: 0.7 }}>
    {PROJECT_META.date} · School of Sciences and Engineering
  </p>
</footer>
```

---

## 16. GRID PATTERNS

### Common Grid Templates

| Pattern | gridTemplateColumns | gap | Usage |
|---------|-------------------|-----|-------|
| 2-col even | `1fr 1fr` | `1.25rem` | Side-by-side images, paired content |
| 3-col even | `repeat(3, 1fr)` | `1.25rem` | Photo grids, triple cards |
| 4-col even | `repeat(4, 1fr)` | `1rem` | Stats row, step sequence |
| Asymmetric | `1.2fr 0.8fr` | `1.25rem` | Image + description |
| Auto-fit | `repeat(auto-fit, minmax(280px, 1fr))` | `1.25rem` | Responsive card grids |

### Stats Row Pattern
```jsx
<div style={{ display: 'flex', gap: '1rem', flexWrap: 'wrap' }}>
  <StatCard ... />
  <StatCard ... />
  <StatCard ... />
  <StatCard ... />
</div>
```

---

## 17. RESPONSIVE STRATEGY

- **No media queries.** All responsiveness via CSS Grid `auto-fit/minmax`, flexbox `wrap`, and `maxWidth` constraints.
- Cards use `flex: '1 1 180px', minWidth: 160` for fluid sizing.
- Images use aspect ratio via `paddingBottom` percentage.
- Content maxWidth: `1200px` centered.

---

## 18. Z-INDEX HIERARCHY

| Layer | zIndex | Element |
|-------|--------|---------|
| Background | 0 | Video/image |
| Gradient overlay | 1 | Gradient div |
| Hero content | 5 | Content card, floating stats |
| Scroll indicator | 10 | Bouncing mouse pill |
| Navigation | 50 | Sticky tab bar |

---

## 19. FILE STRUCTURE CONVENTION

```
public/
├── {name}-showcase.jsx          # React source (source of truth)
├── {name}-showcase.html         # Built self-contained HTML (output)
└── assets/
    ├── AUC/                     # AUC project assets
    │   ├── {course-folder}/     # Original course materials
    │   └── {project-name}/     # Processed project assets
    │       ├── hero-gen/        # Hero video/images
    │       ├── figures/         # Technical figures
    │       ├── diagrams/        # Diagrams, schematics
    │       ├── photos/          # Physical photos
    │       ├── drawings/        # Engineering drawings
    │       ├── renderings/      # 3D renderings
    │       ├── simulations/     # Simulation output images
    │       └── documents/       # PDFs, reports
    └── RU/                      # Rutgers project assets (same structure)
```

### Asset Path Convention
```
/assets/{SCHOOL}/{folder-name}/{subfolder}/{filename}
```

---

## 20. JSX FILE STRUCTURE

Every showcase JSX follows this exact ordering:

```
1. Imports (React, useState, useMemo, useRef, useEffect; Recharts if needed)
2. File header comment (project name, course, student, date)
3. PROJECT_META constant (title, subtitle, student, instructors, date, course, institution)
4. COURSE_HIGHLIGHTS / KEY_METRICS constant (4 items: label, value, sub)
5. TABS constant (array of { id, label })
6. Domain-specific data constants (varies per project)
7. Color palette: const color = { ... }
8. Glass tokens: const glass = { ... }
9. Reusable components: GlassCard, SectionTitle, Pill, StatCard, ImageCard, DataTable, StepCard
10. Domain-specific components (charts, viewers, etc.)
11. Tab content components (one per tab)
12. Main App component (default export):
    a. State declarations (activeTab, hover states)
    b. Font loading via <style> tag (Google Fonts link for Playfair Display)
    c. Return:
       i.   Global background wrapper
       ii.  Hero section
       iii. Navigation bar (sticky)
       iv.  Main content (tabbed)
       v.   Footer
```

---

## 21. GOOGLE FONTS LOADING

Embedded in the JSX via `<style>` tag at component mount:

```jsx
<style>{`@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;500;600;700&display=swap');`}</style>
```

This goes inside the outermost `<div>` of the App component.

---

## APPENDIX A: KNOWN INCONSISTENCIES

These exist in the current AUC showcases. For new RU showcases, always use the **CANONICAL** value.

| Property | Canonical | Deviation | Affected Files |
|----------|-----------|-----------|----------------|
| Hero height | `100vh` | `85vh` | naca0024-cfd |
| Hero H1 fontSize | `2.2rem` | `2.6rem` | naca0024-cfd |
| Hero H1 fontSize | `2.2rem` | `2.4rem` | thesis |
| Hero gradient | `rgba(0,0,0,0.4)…rgba(0,0,0,0.6)` | `rgba(0,0,0,0.3)…rgba(0,0,0,0.5)` | thesis |
| Hero card bg alpha | `0.06` | `0.08` | naca0024-cfd |
| Hero card border alpha | `0.1` | `0.12` | naca0024-cfd |
| Hero H1 fontWeight | `700` | `600` | naca0024-cfd |
| Hero subtitle fontSize | `0.92rem` | `1rem` | naca0024-cfd |
| Hero subtitle opacity | `0.8` | `0.7` | naca0024-cfd |
| Hero subtitle lineHeight | `1.65` | `1.6` | naca0024-cfd, thesis |
| Hero badge fontSize | `0.7rem` | `0.65rem` | naca0024-cfd |
| Hero badge padding | `8px 20px` | `6px 16px` | naca0024-cfd |
| Hero badge letterSpacing | `2px` | `2.5px` | naca0024-cfd |
| Floating stats top | `5%` | `8%` | naca0024-cfd, thesis |
| StatCard variant | Standard (with unit/sub) | Compact (value+label only) | naca0024-cfd, thesis |
| StatCard value fontSize | `1.7rem` | `1.6rem` | naca0024-cfd, thesis |
| StatCard label fontSize | `0.72rem` | `0.65rem` | naca0024-cfd, thesis |
| StatCard label fontWeight | `600` | `500` | naca0024-cfd, thesis |
| StatCard label letterSpacing | `1.5px` | `2.5px` | naca0024-cfd, thesis |
| glass.surface | Defined | Missing | failure-analysis, design-ii |

**Root cause:** NACA-0024 and thesis were built in an earlier iteration before the design system was standardized. The other 5 showcases (system-dynamics, failure-analysis, FEM, AM, design-ii) represent the canonical, finalized pattern.

---

## APPENDIX B: BUILD PIPELINE

### Build Steps (per showcase)
1. Copy `{name}-showcase.jsx` → `showcase-build/src/App.jsx`
2. `npx vite build` from `showcase-build/`
3. Run appropriate inliner:
   - **Generic** (`inline_smart.py`): Most showcases. `--skip-docs` for FEM, failure-analysis.
   - **AM-specific** (`inline_am.py`): Handles `IMG_BASE` + template literal photo paths.
   - **Design-II-specific** (`inline_design_ii.py`): Uses `str.replace()` to avoid `\u` escape conflicts.
4. Output: self-contained HTML with all assets base64-inlined.

### Inliner Flags
- `--skip-docs`: Skips `.pdf, .docx, .pptx, .zip, .stl, .stp, .igs, .dat, .mechdb, .agdb, .SLDPRT, .CATPart, .rth, .rst`

### Master Rebuild
```bash
python3 rebuild_all.py                    # all 7
python3 rebuild_all.py naca0024-cfd fem   # specific ones
```

### Vite Dependencies
```json
{
  "react": "^19.0.0",
  "react-dom": "^19.0.0",
  "recharts": "^2.15.0",
  "three": "^0.170.0",
  "@vitejs/plugin-react": "^4.5.2",
  "vite": "^6.3.5"
}
```
