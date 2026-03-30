# NACA 0024 CFD Showcase — Design Decisions Report
**Comprehensive Design System Analysis**
**Component: naca0024-cfd-showcase.jsx (1,423 lines)**

---

## 1. CSS VARIABLES & DESIGN TOKENS

### Color Palette (Line 142-153)
```javascript
const color = {
  bg: '#f5f5f7',                          // Light gray background
  text: '#1d1d1f',                        // Near-black text
  secondary: '#6e6e73',                   // Medium gray (secondary text)
  tertiary: '#86868b',                    // Light gray (tertiary text)
  accent: '#0071e3',                      // Apple Blue
  accentLight: 'rgba(0,113,227,0.06)',   // 6% opacity accent (backgrounds)
  accentBorder: 'rgba(0,113,227,0.15)',  // 15% opacity accent (borders)
  border: 'rgba(0,0,0,0.06)',            // Subtle dark border (6% opacity)
  white: '#ffffff'
};
```

**Design Decision**: Apple's color system with high-contrast text (1d1d1f), reduced accessibility visual noise with light tertiary colors (#86868b), and accent color matching iOS blue (#0071e3).

---

## 2. GLASSMORPHISM DESIGN TOKENS (Lines 118-140)

### Card Styling
```javascript
const glass = {
  card: {
    background: 'rgba(255,255,255,0.65)',           // 65% opacity white
    backdropFilter: 'saturate(180%) blur(20px)',
    WebkitBackdropFilter: 'saturate(180%) blur(20px)',
    border: '0.5px solid rgba(0,0,0,0.06)',        // 0.5px hairline border
    borderRadius: '16px',
    boxShadow: '0 1px 4px rgba(0,0,0,0.03)'       // Subtle shadow
  },
  cardHover: {
    boxShadow: '0 4px 20px rgba(0,0,0,0.06)',
    transform: 'translateY(-2px)'
  },
  nav: {
    background: 'rgba(255,255,255,0.72)',
    backdropFilter: 'saturate(180%) blur(20px)',
    WebkitBackdropFilter: 'saturate(180%) blur(20px)',
    borderBottom: '0.5px solid rgba(0,0,0,0.06)'
  },
  surface: {
    background: 'rgba(255,255,255,0.45)',
    backdropFilter: 'saturate(120%) blur(12px)',
    WebkitBackdropFilter: 'saturate(120%) blur(12px)',
    border: '0.5px solid rgba(0,0,0,0.04)',
    borderRadius: '14px'
  }
};
```

**Design Decisions**:
- **Blur values**: 20px (cards), 12px (surfaces), 8px (overlays) — graduated intensity
- **Saturation**: 180% (cards/nav), 120% (surfaces) — increases vibrancy behind glass
- **Opacity hierarchy**: 72% (nav) > 65% (cards) > 45% (surface) — visual depth
- **Border opacity**: 0.06 (main), 0.04 (surface) — near-invisible seperators
- **Hover state**: -2px translateY + shadow upgrade (0 1px 4px → 0 4px 20px)
- **WebKit prefix**: Fallback for Safari browser compatibility

---

## 3. TYPOGRAPHY

### Font Families
```javascript
fontFamily: "'Playfair Display', Georgia, serif"     // Headings (SectionTitle, H1)
fontFamily: "'Inter', -apple-system, sans-serif"     // Body text
fontFamily: "'SF Mono', 'Fira Code', monospace"      // Code/equations
```

### Typography Scales

#### Section Titles (SectionTitle component, Line 165-173)
- Font-family: Playfair Display (serif)
- Font-size: 1.5rem (24px)
- Font-weight: 600
- Line-height: default (1.2)
- Letter-spacing: -0.01em (tight tracking)
- Color: color.text (#1d1d1f)
- Margin-bottom: 1.25rem

#### Hero H1 (Line 1166)
- Font-family: Playfair Display
- Font-size: 2.6rem (41.6px)
- Font-weight: 600
- Line-height: 1.15
- Letter-spacing: -0.02em (tighter)
- Color: #ffffff (white on dark overlay)
- Text-shadow: 0 2px 20px rgba(0,0,0,0.5)

#### Hero Subtitle/Paragraph (Line 1173)
- Font-size: 1rem (16px)
- Color: rgba(255,255,255,0.7) (white, 70% opacity)
- Line-height: 1.6

#### Pills/Buttons (Pill component, Line 181-202)
- Font-family: Inter
- Font-size: 0.82rem (13.12px)
- Font-weight: 500
- Letter-spacing: default
- Border-radius: 980px (pill shape)

#### Stat Values (StatCard component, Line 207)
- Font-size: 1.6rem (25.6px)
- Font-weight: 700
- Font-family: Inter

#### Stat Labels (StatCard, Line 209)
- Font-size: 0.65rem (10.4px)
- Font-weight: 500
- Text-transform: uppercase
- Letter-spacing: 2.5px
- Color: color.tertiary

#### Table Headers (DataTable, Line 226)
- Font-size: 0.75rem (12px)
- Font-weight: 600
- Text-transform: uppercase
- Letter-spacing: 1px
- Color: color.text

#### Table Body (Line 239)
- Font-size: 0.85rem (13.6px)
- Font-weight: 400 (default)
- Font-variant-numeric: tabular-nums (fixed-width numbers)

#### Tooltip (Line 252)
- Font-size: 0.8rem (12.8px)
- Font-family: Inter

#### Hero Overlay Label (Line 1149)
- Font-size: 0.65rem
- Font-weight: 600
- Color: #ffffff
- Text-transform: uppercase
- Letter-spacing: 2.5px

#### Hero Date/Meta (Line 1170)
- Font-size: 0.78rem
- Color: rgba(255,255,255,0.45)

#### Footer (Line 1358)
- Font-size: 0.75rem / 0.7rem
- Color: color.tertiary

---

## 4. SPACING & LAYOUT

### Padding Values
```javascript
// Cards & containers
padding: '1.5rem'       // 24px (card default)
padding: '2rem'         // 32px (spacious sections)
padding: '16px 20px'    // 16px vertical, 20px horizontal (objectives)
padding: '1.25rem 1.5rem' // Asymmetric (equation box)
padding: '14px 16px'    // Table headers
padding: '12px 16px'    // Table cells
padding: '10px 14px'    // Photo captions
padding: '1.5rem 2rem'  // Footer

// Buttons
padding: '8px 20px'     // Pills/buttons

// Glass overlay
padding: '2rem 2.5rem'  // Hero overlay container
padding: '12px 18px'    // Floating stats (top-right)
```

### Margin Values
```javascript
margin-bottom: '1.25rem'  // Section titles
margin-bottom: '1rem'     // Paragraphs
margin-bottom: '10px'     // Chart captions
margin-bottom: '1.2rem'   // Hero label
margin-bottom: '0.8rem'   // Hero H1
margin-bottom: '4px'      // Finding titles
margin-bottom: '6px'      // Stat labels
margin: '0 auto'          // Centering
margin-top: '1.5rem'      // Mesh visualization spacing
margin-bottom: '8px 0 0'  // Footer secondary line
```

### Gap Values (Flexbox)
```javascript
gap: '3rem'         // Vertical spacing between major sections
gap: '2rem'         // Grid spacing (2-column layouts)
gap: '1rem'         // Card grids (3-column photos/findings)
gap: '12px'         // Objective cards
gap: '16px'         // Flex containers (pills, objectives)
gap: '20px'         // Finding cards
gap: '14px'         // List items (metadata)
gap: '10px'         // Pill container spacing
gap: '6px'          // Adjacent pills (no margin, just gap)
gap: '1.5rem'       // Mesh image grid
gap: '10px'         // Photo grid (3-column)
```

### Max-width & Container
```javascript
maxWidth: '1200px'      // Main content width
maxWidth: '560px'       // Hero text overlay
maxWidth: '440px'       // Domain SVG
maxWidth: '400px'       // Airfoil profile SVG
```

### Heights
```javascript
height: '85vh'          // Hero section (viewport-based)
minHeight: '520px'      // Hero minimum
maxHeight: '900px'      // Hero maximum
height: '200px'         // Photo cards
height: '380px'         // Chart containers
height: 'auto'          // SVGs, images (responsive)
```

---

## 5. BORDER RADIUS VALUES

```javascript
borderRadius: '16px'    // Primary cards (glass.card)
borderRadius: '14px'    // Secondary surfaces (glass.surface, images)
borderRadius: '12px'    // Equation boxes, chart containers
borderRadius: '20px'    // Video container overflow
borderRadius: '980px'   // Pill buttons (fully rounded)
borderRadius: '50%'     // Perfect circles (numbering badges, icons)
borderRadius: '4px'     // Subtle: bar chart radius tops [4, 4, 0, 0]
borderRadius: '2px'     // SVG paths (C-domain rectangle rx="2")
```

---

## 6. ANIMATIONS & TRANSITIONS

### Keyframe Animations

#### Hero Scroll Indicator (Line 1341-1345)
```javascript
@keyframes heroFloat {
  0%, 100% { transform: translateX(-50%) translateY(0); }
  50% { transform: translateX(-50%) translateY(6px); }
}
// Animation applied: animation: 'heroFloat 2s ease-in-out infinite'
```

### Transition Properties
```javascript
transition: 'all 0.25s ease'        // GlassCard hover (main transition)
transition: 'all 0.2s ease'         // Pills (background, border, color)
transition: 'color 0.2s ease'       // Links (hover state)
transition: 'all 0.2s ease'         // PDF link buttons (background, border, color)
```

### Hover Effects

#### GlassCard Hover (Line 160-164)
```javascript
onMouseEnter={() => setHovered(true)}
onMouseLeave={() => setHovered(false)}
// Applies: boxShadow '0 4px 20px rgba(0,0,0,0.06)' + transform 'translateY(-2px)'
```

#### PDF Link Hover (Line 1189-1194)
```javascript
onMouseEnter={e => {
  e.currentTarget.style.background = 'rgba(0,113,227,0.2)';
  e.currentTarget.style.borderColor = 'rgba(0,113,227,0.4)';
  e.currentTarget.style.color = '#ffffff';
}}
onMouseLeave={e => {
  e.currentTarget.style.background = 'rgba(255,255,255,0.08)';
  e.currentTarget.style.borderColor = 'rgba(255,255,255,0.15)';
  e.currentTarget.style.color = 'rgba(255,255,255,0.75)';
}}
```

#### Instructor Link Hover (Line 1180-1182)
```javascript
onMouseEnter={e => e.currentTarget.style.color = '#60a5fa'}
onMouseLeave={e => e.currentTarget.style.color = 'rgba(255,255,255,0.7)'}
```

---

## 7. HERO SECTION DESIGN

### Dimensions (Line 1101-1108)
```javascript
height: '85vh'              // 85% of viewport
minHeight: '520px'          // Minimum readable height
maxHeight: '900px'          // Maximum height cap
overflow: 'hidden'          // Video contained
background: '#050510'       // Very dark background (near black)
```

### Video Background (Line 1110-1120)
```javascript
position: 'absolute'
top: 0, left: 0
width: '100%', height: '100%'
objectFit: 'cover'          // CSS cover behavior
objectPosition: 'center'
zIndex: 1
src: "/assets/AUC/cfd-project/video/naca0024-hero-animation.mp4"
```

### Gradient Overlays (Line 1122-1133)
```javascript
// Dual-layer gradient overlay
background: 'linear-gradient(180deg, rgba(0,0,0,0.4) 0%, transparent 35%, transparent 55%, rgba(0,0,0,0.6) 100%)'
// Effect: Darkens top (0.4 → transparent @ 35%), deepens bottom (0.6 @ 100%)
zIndex: 2
```

### Glass Text Overlay Container (Line 1135-1156)
```javascript
position: 'absolute'
bottom: '12%'
left: '5%'
zIndex: 10
maxWidth: '560px'

// Inner glass container:
background: 'rgba(255,255,255,0.08)'
backdropFilter: 'saturate(140%) blur(24px)'
border: '0.5px solid rgba(255,255,255,0.12)'
borderRadius: '20px'
padding: '2rem 2.5rem'
boxShadow: '0 8px 32px rgba(0,0,0,0.3), inset 0 0.5px 0 rgba(255,255,255,0.1)'
// Inset shadow creates inner light edge
```

### Hero Label Pill (Line 1157-1167)
```javascript
padding: '6px 16px'
borderRadius: '980px'
background: 'rgba(255,255,255,0.12)'
border: '0.5px solid rgba(255,255,255,0.25)'
fontSize: '0.65rem'
fontWeight: 600
color: '#ffffff'
textTransform: 'uppercase'
letterSpacing: '2.5px'
backdropFilter: 'blur(8px)'
```

### Floating Stats (Top-right, Line 1202-1226)
```javascript
position: 'absolute'
top: '8%'
right: '5%'
zIndex: 10
display: 'flex'
gap: '10px'

// Each stat card:
background: 'rgba(255,255,255,0.06)'
backdropFilter: 'blur(16px)'
border: '0.5px solid rgba(255,255,255,0.1)'
borderRadius: '14px'
padding: '12px 18px'
boxShadow: '0 4px 16px rgba(0,0,0,0.2)'
```

### Scroll Indicator (Line 1228-1247)
```javascript
position: 'absolute'
bottom: '4%'
left: '50%'
transform: 'translateX(-50%)'
zIndex: 10
opacity: 0.4
animation: 'heroFloat 2s ease-in-out infinite'

// Inner scroll icon:
width: '20px', height: '32px'
borderRadius: '10px'
border: '1.5px solid rgba(255,255,255,0.4)'
```

---

## 8. NAVIGATION/TABS DESIGN

### Tab Bar (Line 1277-1289)
```javascript
// Glass-styled sticky nav
...glass.nav
position: 'sticky'
top: 0
zIndex: 50
padding: '12px 0'

// Container
maxWidth: '1200px'
margin: '0 auto'
display: 'flex'
gap: '0.5rem'
justifyContent: 'center'
flexWrap: 'wrap'
padding: '0 2rem'
```

### Pill Buttons (Pill component, Line 175-202)
```javascript
padding: '8px 20px'
borderRadius: '980px'
fontSize: '0.82rem'
fontWeight: 500
fontFamily: "'Inter', -apple-system, sans-serif"

// Active state:
border: 'none'
background: color.accent (#0071e3)
color: '#fff'

// Inactive state:
border: `0.5px solid ${color.accentBorder}` (rgba(0,113,227,0.15))
background: 'transparent'
color: color.accent

transition: 'all 0.2s ease'
cursor: 'pointer'
```

---

## 9. SECTION LAYOUT PATTERNS

### Full-Width Sections
```javascript
display: 'flex'
flexDirection: 'column'
gap: '3rem'           // Vertical rhythm
```

### 2-Column Grid Layouts
```javascript
display: 'grid'
gridTemplateColumns: '1fr 1fr'
gap: '2rem'
```

### 3-Column Photo/Card Grids
```javascript
display: 'grid'
gridTemplateColumns: 'repeat(3, 1fr)'
gap: '1rem'           // Tight grid spacing
```

### 4-Column Stats Grid
```javascript
display: 'grid'
gridTemplateColumns: 'repeat(4, 1fr)'
gap: '1rem'
```

### Main Content Container (Line 1292-1295)
```javascript
maxWidth: '1200px'
margin: '0 auto'
padding: '3rem 2rem 4rem'
```

---

## 10. CARD COMPONENTS

### GlassCard (Lines 160-171)
```javascript
// Reusable component with hover option
...glass.card
transition: 'all 0.25s ease'
onMouseEnter/Leave: hover state management

// Hover applications:
hover={true}  → enables hover effects
hover={false} → disables on non-interactive cards
```

### Stat Card (Lines 203-218)
```javascript
// Self-contained stat display
padding: '1.5rem 1rem'
textAlign: 'center'
display: 'flex', flexDirection: 'column', gap: '16px'

Value: fontSize: '1.6rem', fontWeight: 700
Label: fontSize: '0.65rem', textTransform: 'uppercase', letterSpacing: '2.5px'
```

### Finding Cards (AnalysisTab, Line 1050)
```javascript
padding: '1.5rem'
borderTop: `3px solid ${accent}`  // Colored accent top border
```

---

## 11. CHARTS & DATA VISUALIZATION (Recharts)

### Chart Container
```javascript
ResponsiveContainer width="100%" height={380}
margin={{ top: 10, right: 30, left: 10, bottom: 10 }}
```

### Chart Grid (CartesianGrid)
```javascript
strokeDasharray: '3 3'
stroke: color.border (rgba(0,0,0,0.06))
```

### Axes (XAxis/YAxis)
```javascript
stroke: color.tertiary (#86868b)
tick={{ fontSize: 12 }}

label: {
  fontSize: 12,
  fill: color.secondary (#6e6e73),
  position: 'insideBottom' | 'insideLeft'
}
```

### Tooltip Style (Line 251-260)
```javascript
contentStyle: {
  background: 'rgba(255,255,255,0.85)',
  backdropFilter: 'blur(20px)',
  border: `0.5px solid ${color.border}`,
  borderRadius: '12px',
  boxShadow: '0 4px 16px rgba(0,0,0,0.08)',
  fontFamily: "'Inter', -apple-system, sans-serif",
  fontSize: '0.8rem'
}
labelStyle: { color: color.text, fontWeight: 600 }
```

### Line Charts (CFD vs Literature)
```javascript
// CL vs Alpha (Line 905)
LineChart data={CFD_VS_LIT}
Line: dataKey="clCfd"
  stroke: color.accent (#0071e3)
  strokeWidth: 2
  dot: {{ fill: color.accent, r: 4, strokeWidth: 0 }}
Line: dataKey="clLit"
  stroke: '#ff9f0a' (orange)
  strokeWidth: 2
```

### Mesh Comparison Charts (Line 945-960)
```javascript
// Multiple overlaid lines
Line: "coarse" → stroke: '#ff453a' (red)
Line: "medium" → stroke: '#ff9f0a' (orange)
Line: "fine" → stroke: color.accent (blue), strokeWidth: 2
```

### Bar Charts (CL Error, Line 1000-1015)
```javascript
BarChart data={CL_ERR}
Bar colors: '#ff453a' (red), '#ff9f0a' (orange), color.accent (blue)
radius: [4, 4, 0, 0]  // Top-rounded only
opacity: 0.8
```

### Legend (all charts)
```javascript
wrapperStyle: {{ paddingTop: '12px', fontSize: '0.82rem' }}
```

---

## 12. DATA TABLE COMPONENT (Lines 220-250)

```javascript
// Glassmorphic table wrapper
...glass.surface
overflowX: 'auto'
borderRadius: '14px'

// Table styling
borderCollapse: 'collapse'
fontSize: '0.85rem'
fontFamily: "'Inter', -apple-system, sans-serif"

// Headers
padding: '14px 16px'
fontWeight: 600
fontSize: '0.75rem'
textTransform: 'uppercase'
letterSpacing: '1px'
borderBottom: `1px solid ${color.border}`

// Body rows
padding: '12px 16px'
borderBottom: `0.5px solid ${color.border}` (except last row)
fontVariantNumeric: 'tabular-nums'  // Fixed-width numbers
```

---

## 13. INTERACTIVE ELEMENTS & STATES

### Button Hover (PDF links, Line 1189-1194)
```javascript
Default:
  background: 'rgba(255,255,255,0.08)'
  border: '0.5px solid rgba(255,255,255,0.15)'
  color: 'rgba(255,255,255,0.75)'

Hover:
  background: 'rgba(0,113,227,0.2)'
  border: '0.5px solid rgba(0,113,227,0.4)'
  color: '#ffffff'
```

### Link Hover (Instructor link, Line 1180-1182)
```javascript
Default: color: 'rgba(255,255,255,0.7)'
Hover: color: '#60a5fa' (light blue)
transition: 'color 0.2s ease'
```

### Pill Button States
```javascript
Active:
  border: 'none'
  background: #0071e3
  color: '#ffffff'

Inactive:
  border: `0.5px solid rgba(0,113,227,0.15)`
  background: 'transparent'
  color: #0071e3

transition: 'all 0.2s ease'
```

---

## 14. MEDIA & RESPONSIVE PATTERNS

### Video Players
```javascript
// Hero video (Line 1110-1120)
position: 'absolute', full bleed
width: '100%', height: '100%'
objectFit: 'cover'
autoPlay, loop, muted, playsInline

// Embedded video (OverviewTab, Line 449-458)
width: '100%'
height: 'auto'
borderRadius: '20px'
src: "/assets/AUC/cfd-project/video/naca0024-cfd-animation.mp4"
```

### Image Cards
```javascript
// Photo grid images (Line 467-477)
width: '100%'
height: '200px'
objectFit: 'cover'
display: 'block'
loading: 'lazy'

// Captions overlay (Line 479-486)
position: 'absolute'
bottom: 0, left: 0, right: 0
padding: '24px 12px 10px'
background: 'linear-gradient(to bottom, transparent, rgba(0,0,0,0.6))'
color: '#ffffff'
```

### Contour Image Viewer (Line 765)
```javascript
borderRadius: '12px'
overflow: 'hidden'
background: '#fafafa'
border: `0.5px solid ${color.border}`
position: 'relative'
```

---

## 15. SVG VISUALIZATIONS

### Airfoil Profile (OverviewTab, Line 418-449)
```javascript
viewBox="0 0 400 300"
width: '100%', maxWidth: '400px'

Defs:
  linearGradient: 0% opacity accent → 100% 8% opacity accent

Elements:
  Grid lines: stroke: color.border, strokeWidth: 0.5
  Airfoil path: stroke: color.accent, strokeWidth: 1.5
  Chord line: dashed, opacity: 0.4
  Labels: Playfair Display serif, font-size 13
```

### Computational Domain (MethodologyTab, Line 515-704)
```javascript
viewBox="0 0 460 360"
width: '100%', maxWidth: '440px'

Background:
  Dark gradient: linear-gradient(135deg, rgba(5,5,16,0.97), rgba(15,20,40,0.97))

Elements:
  Subtle grid: stroke: rgba(96,165,250,0.06)
  C-domain arc: stroke: #60a5fa, opacity: 0.5
  Airfoil fill: linear-gradient metallic gray
  Flow streamlines: stroke: #60a5fa, various opacities
  Dimension lines: dashed rgba(96,165,250,0.25)

Filters:
  feGaussianBlur stdDeviation: 3 (airfoil glow)

Markers:
  arrowBlue: fill #60a5fa, opacity 0.6
  arrowDim: fill #60a5fa, opacity 0.4
```

---

## 16. FOOTER (Lines 1354-1362)

```javascript
borderTop: `0.5px solid ${color.border}`
padding: '2rem'
textAlign: 'center'

Heading: fontSize: '0.75rem', color: color.tertiary
Subheading: fontSize: '0.7rem', color: color.tertiary, opacity: 0.7
```

---

## 17. RESPONSIVE BREAKPOINTS & MOBILE CONSIDERATIONS

**No explicit media queries found** — Component uses:
- **Flexible grid**: `gridTemplateColumns: 'repeat(3, 1fr)'` flows naturally
- **Padding**: Consistent 2rem sidescroll padding prevents edge-crush
- **FlexWrap**: `flexWrap: 'wrap'` on pill container adapts to narrow screens
- **maxWidth**: 1200px container prevents excessive line-length
- **ViewBox SVGs**: Scale responsively with aspect-ratio preservation
- **Images**: 100% width, height auto, lazy loading

---

## 18. DESIGN SYSTEM HIERARCHY

### Visual Weight Hierarchy
1. **Hero video + overlay** (85vh, full-bleed)
2. **Section titles** (1.5rem Playfair, -0.01em tracking)
3. **Body text** (0.95rem, 1.6 line-height)
4. **Secondary text** (0.85rem, color.secondary)
5. **Tertiary labels** (0.65–0.75rem, uppercase, 1–2.5px spacing)

### Color Weight Hierarchy
1. **Primary accent**: #0071e3 (interactive elements)
2. **Secondary accents**: #ff9f0a (orange), #ff453a (red) — data viz
3. **Text hierarchy**: text (#1d1d1f) > secondary (#6e6e73) > tertiary (#86868b)
4. **Backgrounds**: White with reduced opacity (glass effect)

### Spacing Rhythm
- **Major sections**: 3rem gap
- **Layout grids**: 2rem gap
- **Card groups**: 1rem gap
- **Internal card padding**: 1.5–2rem

---

## 19. SPECIAL COMPONENTS

### Photo Gallery Grid (Line 464-487)
- 3-column layout on desktop
- 1rem gap between cards
- Images: 200px height, cover fill
- Lazy loading enabled
- Gradient overlay for caption text

### Objectives List (Line 359-381)
- Numbered circles: 28px, centered badge
- Background: color.accentLight
- Color: color.accent
- Font-weight: 600

### Mesh Parameters Table (Line 724-738)
- DataTable component
- 7-column layout
- Centered alignment except first column
- Tabular number formatting

### Findings Cards (AnalysisTab, Line 1048-1060)
- 3-column grid
- Colored top border (3px): accent, orange, red
- Left-aligned text
- Fixed width container

---

## 20. COMPUTED/DYNAMIC STYLING

### Contour Viewer Selector (Line 747-773)
```javascript
// Dynamic src construction:
src={`/assets/AUC/cfd-project/contours/naca0024-${contourType === 'vectors' ? 'vectors' : contourType}-${meshDensity}.png`}

// Active pill state managed via onClick callbacks
```

### Chart Data Transformation (Line 870-877)
```javascript
// Mesh overlay combines 3 datasets into single chart
const meshOverlayCD = MESH_DATA.medium.map((m, i) => ({
  re: (m.re / 1e6).toFixed(2),
  medium: m.cd,
  coarse: MESH_DATA.coarse[i].cd,
  fine: MESH_DATA.fine[i].cd
}));
```

---

## KEY DESIGN SYSTEM TAKEAWAYS

### Consistency Patterns
1. **16px baseline**: borderRadius values scale (14px, 16px, 20px, 980px)
2. **Blur & saturation**: Graduated (24px/180% → 12px/120% → 8px)
3. **Opacity tiers**: 72%, 65%, 45%, 12%, 8%, 6%, 4% for defined hierarchy
4. **Gap rhythm**: 3rem → 2rem → 1rem (3:2:1 ratio)
5. **Font hierarchy**: 2.6rem → 1.5rem → 1rem → 0.95rem → 0.85rem → 0.75rem

### Glass Design Principles
- **Always paired**: backdropFilter + WebkitBackdropFilter (Safari)
- **Light borders**: 0.5px with extreme opacity (0.04–0.15)
- **Inset highlights**: `inset 0 0.5px 0 rgba(255,255,255,0.1)` for depth
- **Subtle shadows**: Max 0.08 opacity on dark overlay

### Accessibility Considerations
- **Text contrast**: #1d1d1f on #f5f5f7 (21:1 WCAG AAA)
- **Interactive targets**: Pills min 8px padding, all have hover states
- **Semantic HTML**: table with proper thead/tbody
- **Lazy image loading**: Reduces initial payload

