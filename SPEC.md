# Clarity — Product Specification

> Screen Time & Focus Companion for iPhone + Mac

---

## 1. Concept & Vision

**Tagline:** _Reclaim your attention._

Clarity is a mindful screen time companion that helps you understand your phone habits without the creepy surveillance feel. Where other apps scream "YOU'RE DOING BADLY," Clarity whispers "Here's what's happening, and here's how to take control — on your terms."

The experience is **calm, beautiful, and empowering**. Think of it as a meditation app that happens to track your screen time, not a surveillance tool that happens to have a nice UI.

The companion Mac app transforms your Mac into a "Focus Sanctuary" — when you're working, Clarity on your Mac quietly blocks distracting sites, and you control it all from your iPhone. The feeling: **your tools are working together to protect your attention**.

---

## 2. Design Language

### Aesthetic Direction
**Reference:** Calm app meets Linear meets a Japanese zen garden.

Soft, desaturated pastels on dark backgrounds. Generous whitespace. Typography that breathes. Rounded corners everywhere. The UI should feel like taking a deep breath.

### Color Palette
```
Background Primary:   #0F0F13 (near-black with blue undertone)
Background Secondary: #1A1A21 (card backgrounds)
Surface:             #24242E (elevated elements)
Accent Primary:       #7C6AFF (soft purple — calm, focused)
Accent Secondary:     #5EEAD4 (mint teal — for positive states)
Accent Warm:          #F59E0B (amber — for warnings, streaks)
Text Primary:         #F4F4F6 (off-white)
Text Secondary:       #8B8B9E (muted)
Text Tertiary:        #55556A (very muted)
Border:               #2E2E3A (subtle dividers)
Success:              #34D399 (emerald)
Destructive:          #F87171 (soft red)
```

### Typography
- **Headings:** SF Pro Rounded (iOS native, weight 600-700)
- **Body:** SF Pro Text (weight 400-500)
- **Numbers/Stats:** SF Mono (for timers, numbers — distinct, technical feel)
- **Fallback:** -apple-system, system-ui

### Spatial System
- Base unit: 4pt
- Component padding: 16pt
- Card radius: 20pt
- Button radius: 14pt
- Section spacing: 32pt

### Motion Philosophy
- **Principle:** Motion should feel like breathing — natural, unhurried, smooth.
- Default: 300ms ease-out
- Spring animations for interactive elements (damping 0.8, response 0.4)
- Timer animations: smooth CADisplayLink-driven arcs
- Screen transitions: 250ms cross-dissolve
- Numbers change: animated count-up/down

### Visual Assets
- Icons: SF Symbols (filled variant for active, regular for inactive)
- Charts: Custom SwiftUI paths — no external charting library
- Gradients: Subtle purple-to-teal accent gradients for highlights
- Blurs: Ultra thin material for overlays (iOS blur style)

---

## 3. App Architecture

### Platforms
1. **Clarity iOS** — Main app (SwiftUI, iOS 17+)
2. **Clarity Mac** — Menu bar app (AppKit + SwiftUI, macOS 14+)

### Shared
- CloudKit for data sync (private database)
- App Group for local shared data (UserDefaults suite)

### Data Model

```
User
  - id: UUID
  - createdAt: Date
  - settings: Settings

Settings
  - dailyScreenGoal: Int (minutes)
  - notificationsEnabled: Bool
  - windDownStart: Date (time of day)
  - premiumActive: Bool

FocusSession
  - id: UUID
  - startTime: Date
  - endTime: Date?
  - duration: Int (seconds)
  - mode: FocusMode
  - completed: Bool
  - blockedCount: Int (how many distractions blocked)

FocusMode
  - name: String
  - workDuration: Int (seconds)
  - breakDuration: Int (seconds)
  - color: String (hex)

DailySummary
  - id: UUID
  - date: Date
  - totalScreenTime: Int (minutes)
  - focusMinutes: Int
  - topApps: [AppUsage]
  - sessionsCompleted: Int
  - goalMet: Bool

AppUsage
  - appName: String
  - bundleId: String
  - minutes: Int
  - icon: Data?

WindDownSession
  - id: UUID
  - startTime: Date
  - duration: Int (minutes)
  - activities: [WindDownActivity]

WindDownActivity
  - type: ActivityType (reading, journaling, stretching, meditation, none)
  - completed: Bool
```

---

## 4. Screen Structure

### iOS App Screens

**Tab 1: Today (Home Dashboard)**
- Greeting with time-of-day message
- Screen time ring (today vs goal)
- Focus session quick-start button
- Top 3 most-used apps today
- Streak counter
- Quick stats row (sessions, focus minutes, longest session)

**Tab 2: Focus**
- Focus mode selector (cards)
- Timer display (large, centered)
- Ambient sound selector
- Session in progress UI (minimal, calming)
- Session history list

**Tab 3: Insights**
- Weekly screen time bar chart
- Focus trend line chart
- "Your best day" highlight
- AI-generated insight card
- Most distracted times heatmap

**Tab 4: Wind Down**
- Pre-sleep ritual builder
- Current time + wind down progress
- Activity cards (read, journal, stretch, meditate)
- Tomorrow's focus preview
- Sleep quality correlation (if HealthKit available)

**Tab 5: Settings**
- Daily screen goal slider
- Notification preferences
- Focus modes management
- Mac companion pairing
- Premium upgrade
- About / Help

### Mac Menu Bar App
- Menu bar icon (shows current state: idle/focusing/break)
- Dropdown: Today's stats summary
- Quick start focus session
- Blocked sites/apps count
- "Open Clarity iOS" link
- Quit

---

## 5. Core Features (Priority Order)

### Must-Have (P1) — Launch Scope
1. **Screen Time Dashboard** — beautiful ring showing today's usage vs goal
2. **Focus Timer** — Pomodoro with customizable work/break modes
3. **Focus Modes** — 3 presets (Deep Work 50/10, Classic 25/5, Flow 90/20)
4. **Ambient Sounds** — 8 synthesized soundscapes
5. **Session History** — list of past sessions with stats
6. **Daily Streak** — consecutive days with ≥1 focus session
7. **Basic Insights** — today's summary, weekly trend
8. **Mac Companion Ready** — UI ready, stub for connection

### Should-Have (P2) — Post-Launch
9. **Wind Down Mode** — pre-sleep ritual cards
10. **App Usage Breakdown** — top apps today (via Screen Time API)
11. **Focus Score** — composite 0-100 score
12. **Achievement Badges** — milestone celebrations
13. **Weekly Report** — push notification with Monday summary
14. **Mac Menu Bar App** — actual site/app blocking
15. **CloudKit Sync** — seamless iPhone + Mac data

### Nice-to-Have (P3)
16. **AI Insights** — personalized tips based on patterns
17. **Social Sharing** — beautiful card to share focus wins
18. **iOS Widget** — small/medium widget for home screen
19. **Apple Health Sync** — correlate sleep and focus
20. **Focus Party** — synchronized group focus sessions

---

## 6. Technical Approach

### iOS App
- **UI:** SwiftUI (iOS 17+)
- **Architecture:** MVVM with ObservableObject ViewModels
- **Data:** UserDefaults (local) + CloudKit (sync, premium)
- **Screen Time:** Screen Time API (DeviceActivity framework)
- **Audio:** AVAudioEngine (synthesized ambient sounds — same as FocusTimer)
- **Widgets:** WidgetKit
- **App Group:** group.com.clarity.app (shared between iOS + Mac)

### Mac Menu Bar App
- **UI:** AppKit NSStatusItem + SwiftUI popover
- **Architecture:** AppKit delegate + SwiftUI views
- **Site Blocking:** DeviceActivity + Content Blocker (Safari extension)
- **IPC:** App Group UserDefaults + CloudKit

### Dependencies
- None (pure native — keeps build simple on cloud Mac)

---

## 7. Monetization

### Free Tier
- Today's screen time ring
- 3 focus modes
- 8 ambient sounds
- 7-day session history
- Basic daily summary

### Premium ($4.99/month or $39.99/year)
- Unlimited session history
- All focus modes + custom modes
- Mac companion app + blocking
- AI weekly insights
- Unlimited wind down rituals
- Widgets
- Export data (CSV)
- No ads, ever

### Launch Strategy
- Launch with free tier only, collect reviews
- Add premium after 500+ downloads
- Focus on Product Hunt + indie communities

---

## 8. Success Metrics (First 30 Days)

- Downloads: 1,000+
- Active users (7-day retention): 30%+
- Average sessions per user: 2.5/day
- App Store rating: 4.5+
- Revenue (if premium launched): $500+

---

## 9. Competitive Differentiation

| Competitor | Their Weakness | Clarity's Edge |
|---|---|---|
| Screen Time (Apple) | No features, no motivation | Beautiful UI + gamification |
| Digital Detox | Ugly, invasive, creepy | Calm, empowering design |
| Freedom | Complex, expensive, dated UI | Simple, modern, affordable |
| Forest | Game-y, not serious | Focused, calm, non-game |
| BeFocused | Basic, utilitarian | Premium design + insights |

Clarity's unfair advantage: **design sensibility of a top-100 App Store app** + **Mac companion** that no other screen time app offers well.

---

_Last updated: 2026-04-12_
