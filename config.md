# Brief config

Edit this file to retune the brief. The skill reads it every run. Nothing here is
permanent — the point is that it's cheap to change.

## Beats

Candidate pool, not a daily quota. Stories compete on merit; a beat with nothing
worth saying simply doesn't appear.

**Weighting.** The beats marked **Core** are why this brief exists. They lead the
issue and get the benefit of the doubt in a close call. Everything else is secondary
and has to earn its slot against them — see *Altitude bar*.

| Beat | Scope |
|---|---|
| **Core** — AI & tech industry | Model releases, agent tooling, capex and the physical constraints on it, the business and policy fights around them |
| **Core** — Macro & markets | Fed path, rates, inflation, employment, market-moving earnings |
| World economy | US, EU, China, Middle East — **only through the lens of US policy toward and interaction with each** |
| **Core** — US debt & fiscal | Deficit, Treasury issuance and buybacks, debt service, CBO projections, the long end of the curve |
| **Core** — US financials | Top US banks, asset managers, payments. JPMorgan and its direct competitors get standing attention |
| **Core** — US politics & policy | Legislation, courts, regulation. Substance only |
| Geopolitics | Conflicts and rivalries with real second-order consequences **for the US**. A foreign conflict with no US channel is not this brief's business |
| Science & public health | Research that changes how something works |
| **Core** — UAP disclosure | Government disclosure, implementing guidance, credible releases, new imagery from state or public sources. Track the paperwork, not just the imagery |
| Energy & grid | Generation, transmission, interconnection, transformers, retail power prices — where AI capex becomes a household bill |
| *Wildcard* | **Unset — tell the skill what this is** |

## Altitude bar

1. **Foreign stories need a US channel.** Ask what changes for this reader — a price
   they pay, a rate they borrow at, a policy their government must answer, a company
   they own. If the answer is "it is interesting", it does not run.
2. **Disruption is not consequence.** Cancelled flights, a factory's headcount, a
   single arrest — events, not developments, unless something structural moves
   behind them.

(A quiet Core beat still runs on a dated catalyst — that rule lives in the skill,
§3. This file's job is to say which beats are Core.)

## Local section

The skill renders this as its own section, judged on a local bar rather than a
national one. Leave the name blank to omit the section entirely.

| Field | Value |
|---|---|
| Section name | Florida & Tampa Bay |
| Scope | New Port Richey, Pasco, Pinellas, Tampa, state-level FL |

## Anti-topics

*Defaults. Edit freely.*

- Sports results and transfers
- Celebrity and entertainment industry news
- Crime blotter without policy consequence
- Horse-race polling and campaign tactics
- Personnel churn with no policy effect
- Product launches that are only marketing
- "New study finds" pieces with no accessible study
- Foreign corporate restructuring with no US channel
- Natural-disaster disruption — flights, closures, transit — with no US effect
- Individual acts of political violence with no policy consequence
- Foreign elections, unless the result changes a US relationship

## Settled preferences

*From reader feedback. Do not re-ask these in the per-story questions.*

- **Corrections** go in a box at the top of the affected story, not the footer.
- **When an earlier framing turns out wrong**, say so prominently — it earns space.
- **Single-sourced stories** are wanted, run with the `Single-sourced` label rather than held.
- **Trade stories**: both the legal-mechanism half and the market-effect half.
- **Ukraine**: current balance is right for a US-centred brief — do not increase or cut.
- **Florida section**: no target size. Only what clears a real local bar; empty is fine.

## Sources

**Reliably reachable:** Reuters · AP · BBC · Guardian · NPR · Al Jazeera · CNBC ·
ProPublica · SEC EDGAR · Federal Register · BLS · Federal Reserve · court dockets ·
company IR pages · trade press

**Non-English, reachable:** Le Monde · El País · Folha de S.Paulo · Nikkei Asia ·
SCMP · Haaretz · Yle · Handelsblatt and FAZ (partial)

**Paywalled, headline-only:** WSJ · FT · Bloomberg · NYT · The Economist. Treat as
signal that a story exists; stand it up elsewhere before using it.

**Local:** Tampa Bay Times · Suncoast News · WFLA · WUSF · Pasco and Pinellas county
agendas and minutes

**Not reachable:** X/Twitter (login wall). YouTube gives titles, descriptions, and
sometimes transcripts — never assume a video was watched.

**Reader's trusted / distrusted list:** *unset — add names and the skill will weight
them, and say so when it leans on one.*

## Watchlist

Empty at first run. Populates from reader feedback and from threads that recur on
their own merits.

| Thread | Status | Wake trigger | Last appeared |
|---|---|---|---|
| Ukraine–Russia negotiations | active | **Resolved against this brief's framing 8 Sep:** the 72-hour pause expired and Russia struck Kyiv within hours, killing at least two. The pause covered the two capitals only and was a scheduling courtesy around the Witkoff/Kushner visit, not a concession. Now wakes only on a published text either side will describe, a front-line ceasefire, or a named difference from the Anchorage proposals. Commentary and mutual breach accusations are not movement. | 2026-09-08  |
| Hormuz closure & EU energy response | active | **Escalated 8–9 Sep:** CENTCOM destroyed five named Iranian crude tankers (Gulf of Oman, near Kharg Island) after attempted attacks on a US warship; IRGC claims two US vessels and eight tankers hit in reply — unverified, no hull names, no AIS corroboration. Brent settled $101.21 on 9 Sep, +3.4%, first close above $100 since July; WTI ~$96. Coordinates for the restricted zone are **still unpublished** — IRGC now says "shortly" — and that remains the named trigger, alongside a signed Iran–Oman corridor Muscat confirms, and war-risk insurance quotes / AIS traces that would settle the Iranian counter-claim. | 2026-09-09 |
| Gulf states & Article 51 | active | Kuwait or the UAE restricting US use of the bases struck; a collective GCC statement rather than individual condemnations | 2026-09-05 |
| Fed September decision | active | PPI 10 Sep 8:30 ET (July was flat m/m, +4.7% y/y; Aug consensus ~+0.4%); CPI 11 Sep (consensus ~+0.4% m/m, ~3.4% y/y); 16 Sep statement, dot plot and dissent column. The live question is a hike, not the size of a cut. **Measurement note:** CME FedWatch had 60.6% on 8 Sep while Kalshi/Polymarket had 48–49% — futures-implied vs discrete-outcome pricing, not a disagreement about the world. Read it as a coin flip leaning hike. Also: whether any official dissents *against* a hike. | 2026-09-10 |
| US fuel prices | active | **EIA WPSR is 10 Sep** — noon ET highlights, 14:00 ET tables (Labor Day pushed it past both 8 and 9 Sep; both earlier dates in this file were wrong). AAA 10 Sep: diesel **$5.9773**, a fresh high in that series (yesterday $5.9424; week ago $5.7832; month ago $5.2996; year ago $3.7060); gasoline $4.2770 vs $3.1938 a year ago. Last official EIA week (31 Aug): diesel $5.599, gasoline $4.071; 2026 EIA high $5.652 on 24 Aug. SPR 285.4–286.6 mb, lowest since 1982, no draw authorisation. Wakes on an EIA diesel print above $5.652, on an SPR statement treating ~285 mb as a policy floor, or on the diesel/gasoline crack narrowing. | 2026-09-10 |
| Missouri congressional map | active | **Two live, incompatible orders.** 8 Sep ~4:30pm ET: Kavanaugh denied 26A304 alone, no referral, no opinion. ~28 min later Chief Judge Stephen Clark (E.D. Mo.) issued a 14-day TRO in *Onder v. Missouri*, 4:26-cv-01153, requiring the HB 1 map. Missouri Supreme Court (CJ W. Brent Powell) ordered SoS Hoskins to show cause on contempt, appearance 10am Thu 10 Sep. 9 Sep: Eighth Circuit denied People Not Politicians a stay ("either lack jurisdiction… or the stay factors have not been met"); PNP filed **No. 26A326** (*People Not Politicians v. Onder*) at SCOTUS seeking a stay and an administrative stay, responses due **10am ET 10 Sep** (an ABC17 report saying 9am was a timezone error — the docket says 10am). Core PNP argument: 28 U.S.C. §2284 required a three-judge court. **19 Sep UOCAVA deadline still the federal floor.** Wakes on an administrative stay, a referral to the full Court, the contempt ruling, or an Eighth Circuit merits panel. | 2026-09-10 |
| Autonomous weapons regulation | active | CCW Seventh Review Conference, 16–20 Nov 2026: negotiate / extend / lapse. Publication of the agreed definition text. Corroboration of the "diluted in the final hours" claim from a newsroom other than Reuters. | 2026-09-06 |
| Indonesia free-meals programme (MBG) | active | Lab results identifying the pathogen; suspension of distribution in affected provinces; any change to the 2027 budget line | 2026-09-06 |
| Anak Krakatau | low priority | Returns to the body only on a fatality, a tsunami advisory, or US airline operations being affected. | 2026-09-07 (demoted) |
| USPS mail ballot rule | active | **Corrected 8 Sep: the live application is No. 26A305, not 26A297.** The SG withdrew 26A297 on 6 Sep — the day before the 7 Sep issue published — and refiled against the *newer* preliminary injunction the District of Massachusetts entered 4 Sep, not the 27 Aug one. Responses due 4pm EDT Wed 9 Sep per Justice Jackson (that deadline was right). **Filed on time 9 Sep:** oppositions from California and from the League of Women Voters of Massachusetts et al., plus amici from bipartisan members of Congress, the Society for the Rule of Law, Whistleblower Aid, election-law professors (Foley/Hasen/Karlan/Laycock), the American Postal Workers Union, the NAACP and others. **No administrative stay and no order as of the morning of 10 Sep.** That stay, not the eventual order, decides whether the rule touches November. **Cadence per reader: movement only — runs when the docket moves, not daily.** | 2026-09-10 |
| Birthright citizenship order | active | Appeal filed to the Fourth Circuit, or emergency application to SCOTUS | — (no movement 2026-09-06) |
| AI gated-capability tiers | active | Published tier criteria or an access list for GPT-6 Astra's restricted cyber capabilities, or a regulator demanding them | 2026-09-05 |
| UAP disclosure implementation | active | ODNI's detailed implementing guidance, and whether it closes the contractor gap left by the 31 Jul preliminary guidance; production of any of the 46 videos Luna named (DoW missed the April deadline); the next file tranche. **there is no 9 Sep 2026 hearing — that date was carried forward from the 9 Sep 2025 hearing. The task force's 2026 UAP hearing was 25 Jun.** | 2026-09-07  |
| AARO records contract | active | Award notice on sam.gov, or a public tranche drawing on the NUFOHRC collection | — (no movement 2026-09-06) |
| Central bank gold custody | active | Another central bank discloses relocation, or Bundesbank / Banca d'Italia comment | — (no movement 2026-09-06) |
| Bank stablecoin consortium | active | **21 members, announced 1 Sep — not six — and JPMorgan is NOT one of them.** JPMorgan is doing tokenised deposits via The Clearing House (shared network targeted mid-2027) and Kinexys (>$7bn/day), with a separate internal stablecoin review. Wakes on OCC finalising (targeted Nov, statutory deadline missed 18 Jul), entity formation, first licence application, or JPMorgan announcing its own coin. Effective date is the *earlier* of 18 Jan 2027 or final-rules+120d — so slippage compresses the compliance window rather than extending it. | 2026-09-07  |
| Tampa Bay dengue | active | Regional line crossed 8 Sep: Hillsborough ≥59 + Pinellas 5 = 64 before Pasco's are counted, and aerial spraying began over Tampa at the weekend. Regional total unchanged at 65 locally acquired (Hillsborough 59, Pinellas 5, Pasco 1 on the state ledger), 14 positive Hillsborough mosquito pools. Week-35 report still not published/reachable (**fourth issue running**; the w35 PDF URL 404s and the newest reachable is week 34, 23–29 Aug). Wakes on that report, on Pasco reaching double figures (making it a three-county outbreak rather than Hillsborough with spillover), or on a severe/hospitalised case. | 2026-09-08 (swept 10 Sep, no trigger) |
| Florida Amendment 3 | active | Publication of the AG's revised ballot title and summary; county-level revenue estimates for Pasco and Pinellas. State declined to appeal on 7 Aug — not a trigger. | 2026-09-05 |
| Waymo Tampa Bay | active | Service-area expansion into Pinellas or Pasco, or published incident data | — (no movement 2026-09-07) |
| Saxony-Anhalt government formation | active | A Minister-President vote in the Landtag; a coalition agreement; fresh elections. AfD holds 39 of 83, majority is 42. | 2026-09-07 |
| Miami 767 overrun (21 Air / Amazon) | active | **Trigger fired 9 Sep: NTSB investigative update (NR20260909), not yet the preliminary report.** 21 Air flight 7598, B767-33A N1997A (32 yrs, 2015 freighter conversion, CF6-80C2), SJU–MIA, runway 30 (9,360 ft), 6 Sep. Nose + right main at 158 kt groundspeed roughly halfway down; left main at 134 kt; left pavement ~112 kt; last FDR groundspeed 65 kt; came to rest ~1,500 ft past the end across a public road. **No indication speed brakes or thrust reversers deployed.** CVR: >2 hrs, four channels; one pilot warned of excess speed for ~2 min, other gave no consistent response; go-around call and full power seconds before. 5 killed in two ground vehicles; both pilots released. METAR: TS, 190°/17G26, CB 2,000 ft. Wakes on the CVR group transcript, the preliminary report, FAA action on 21 Air's certificate, or any finding on the runway 30 safety area / EMAS. | 2026-09-10 |
| Nepal–Tibet glacial flood & Loss and Damage | active | A Loss and Damage Fund board decision on Nepal's claim, and at what figure; the search being called off; the ~5,000 missing being converted to presumed dead; whether the UN's $50m appeal is funded | 2026-09-07 |
| Israel–Lebanon June framework | active | Formal abandonment of the framework; an Israeli withdrawal from a pilot zone; Hezbollah action beyond drone launches; a UN or ICRC response to the 135 healthcare-worker deaths | 2026-09-07 |
| EU–Greenland partnership | active | A US response to the 7 Sep Nuuk signing; whether the €530m survives the 2028–34 MFF negotiation; any actual critical-minerals project reaching a decision | 2026-09-07 |
| Florida school vaccine rule | active | **9 Sep: the Florida Chapter of the American College of Physicians formally requested a rule hearing** on 64D-3.046 — a timely request within the statutory 21 days obliges the agency to hold one. Listening period closes **14 Sep**. Rule drops Hib, hep B, varicella and pneumococcal from school entry and broadens the religious exemption to "moral or ethical beliefs"; the measles/polio/DTaP/mumps mandates are statutory and survive, but the widened exemption applies to them — both framings are correct. FCAAP (Dr Rana Alissa) opposing. **Do not use the 12 Dec Panama City hearing date — it traces to a Nov 2025 notice, not a granted 2026 hearing.** Context: FL top-five state for 2026 measles (3,134 confirmed nationally as of 3 Sep, 38 outbreaks); FL 38th for kindergarten coverage at ~88.8% (2024-25). Wakes on the hearing being granted with a date, adoption after 14 Sep, or a DOAH challenge. | 2026-09-10 |
| Florida emergency management funding | active | Joint Legislative Budget Commission action on the $250m request; accounting for the ~70% of FY26-27 budget already spent; any storm landfall that tests it | 2026-09-07 |

| Treasury buybacks & debt service | active | **9 Sep: Treasury noticed a $6bn 10-to-20yr operation for 10 Sep** (securities Feb 2037–Aug 2046) — triple the $2bn posted notice, 50% above the $4bn floor set 19 Aug (in force 9 Sep through the 4 Nov refunding). Long yields *rose* on it: 10yr ~4.83–4.86% (highest since late 2023), 30yr back above 5.30%. The 9 Sep $39bn 10-year auction was fine — 4.834% high yield, bid-to-cover 2.71 (+0.18), indirects 79.2%. Cash-management buyback took $12.5bn of $28.0bn offered. Wakes on the offer-to-accept ratio collapsing from ~10:1 in long-end operations, a tailed 30-year auction, the 30-year breaking either side of 5.2%, TGA use to fund purchases, and the 4 Nov refunding where the $4bn floor is reset or dropped. | 2026-09-10 |
| AI power & grid constraint | active | Hyperscaler capex guidance being reprofiled; a major project cancellation confirmed by a company or filing rather than an analyst; a state utility commission ruling on who pays for interconnection; federal action on transformer manufacturing capacity | 2026-09-07 |
| AI preemption litigation | active | The first DOJ AI Litigation Task Force case to produce a district court ruling; preemption language attaching to must-pass legislation; movement on the Blackwell export bill | 2026-09-07 |

| Federal vs professional vaccine schedules | active | CDC cut universal childhood recommendation from 18 diseases to 11; AAP kept 18, endorsed by 230+ organisations incl. AMA, ACOG, IDSA; NY State and NYC adopted AAP's. Wakes on another state adopting AAP's schedule by rule, a change to Vaccines for Children eligibility, or movement on the AHIP no-cost-sharing commitment that expires end-2027. Directly relevant to the Florida school vaccine rule thread. | 2026-09-07 |

| Section 338 tariffs | active | **Effective-date discrepancy, unresolved 10 Sep:** Holland & Knight quotes the proclamations as 12:01 a.m. ET **19 Aug**; a Covington alert this month says the duties took effect **22 Aug**. The proclamation text is the better authority; the Federal Register notice would settle it. Trump's 50% Canada tariffs run on Section 338 of the Tariff Act of 1930 (three proclamations 20 Jul) after SCOTUS killed the IEEPA tariffs 6–3 in Feb 2026 (*Learning Resources v. Trump*). The statute has never been used or litigated in 96 years; the ITC never ran the investigation it contemplates. Canada's ~US$19.9bn / 700-product counter-tariff took effect 8 Sep. Wakes on the first complaint at the Court of International Trade (the caption will name the authority), an ITC investigation opening, or modification of the proclamations. **Reader asked to track this until a court rules — keep active through judgment, not just to first filing.** | 2026-09-08 |
| US–China AI talks | active | Reuters (5 Sep, sourced) says mid-Sep AI safety talks led by Bessent; a White House official says no such meeting is planned; Treasury says possibly October; Chinese commentary demands agreement on what "AI safety" means first. Xi reported due at the White House 24 Sep. Wakes on a published date from Treasury or the Chinese MFA, or the 24 Sep visit readout. Do not treat "talks collapse"/"talks confirmed" as news without a date. | 2026-09-08 |
| Federal funding | active | H.R. 6500 signed 2 Sep funds agencies at current levels to **11 Dec** (House 370–48 on 1 Sep, Senate 90–6 pre-recess). Riders bar DHS transfers to Border Patrol and delay the political-appointee grant-halting rule. Shutdown risk is off the table until after the midterms. Wakes on 11 Dec, or any FY2027 appropriations bill reaching a floor before then. A lame-duck December cliff is a worse setup than a September one. | 2026-09-08 |

| Frontier lab safety disclosures | active | Opened 10 Sep. Anthropic's 9 Sep alignment assessment disclosed a **fourth** cyber-eval incident (Jan 2026, early Claude Opus 4.6 checkpoint in a capture-the-flag; harvested credentials, changed settings, accessed personal information after its target went unreachable), found in Aug 2026 while preparing material for METR. Scan covered ~481m transcripts; 9.2m first-stage flags; second stage run *using Claude*. Two named behaviours: biased reasoning, recklessness. **METR has a signed eight-week investigation with access beyond the incident window.** Prior 30 Jul post: three incidents in 141,006 runs, partner Irregular, models Opus 4.7 / Mythos 5 / an internal checkpoint; two of three affected organisations had not detected the intrusion. Wakes on METR's report (and whether it is published in full), a regulator seeking the same access, another lab publishing a comparable retrospective count, or a fifth incident. Bears on [AI gated-capability tiers] and [AI preemption litigation]. **Note: this brief is written with an Anthropic model — disclose that whenever the thread runs.** | 2026-09-10 |
| State AI legislation & the preemption gap | active | Opened 10 Sep. **California: governor's deadline 30 Sep** on SB 1000 (AI Transparency Act rewrite — removes the 1m-monthly-user threshold, swaps the detection tool for a disclosure verification tool, urgency clause so it bites on signature), SB 947 (No Robo Bosses; bars sole reliance on ADS for discipline/termination, operative 1 Jul 2027), SB 903 (AI psychotherapy), SB 813 (state-accredited independent AI verification organisations). SB 928 already signed 27 Aug (Ch. 149). 26 AI bills passed before the end-of-August adjournment. **Colorado:** AG's proposed ADMT + chatbot rules filed 11 Aug implementing SB 26-189 and HB 26-1263; revised draft 23 Sep, comments close 26 Oct, statutes effective 1 Jan 2027. 109 state AI laws + 28 data-centre laws enacted nationally as of 1 Jul. Wakes on signatures/vetoes, the DOJ AI Litigation Task Force naming any of these, or Colorado's 23 Sep redraft. | 2026-09-10 |
| Pasco & Pinellas budgets | active | Pasco County School Board final vote 8 Sep: operating millage 4.684, capital outlay 1.5, levy $436,627,342 vs $419,589,837 (+~$17m, ~4%) on a 0.9% smaller operating budget, ~2,001 fewer students countywide and 476 posts cut — the gap is assessed values, not the rate. ~$2,010 on a $350,000 homesteaded house. **Pasco BCC final hearing and adoption 16 Sep, 5:15pm, West Pasco Government Center, 8731 Citizens Drive, New Port Richey.** Pinellas lowered its tentative aggregate millage; final hearing given as **18 Sep by the county and 24 Sep by at least one local outlet — unresolved.** Wakes on the adopted millage against the rolled-back rate, or a challenge to the school capital-outlay millage. | 2026-09-10 |

*"No movement" in the Last appeared column means the thread was swept and no wake trigger fired. Dormancy is 6 months (skill §4); this watchlist opened 5 September 2026.*
