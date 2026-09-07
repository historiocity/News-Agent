# Brief config

Edit this file to retune the brief. The skill reads it every run. Nothing here is
permanent — the point is that it's cheap to change.

## Beats

Candidate pool, not a daily quota. Stories compete on merit; a beat with nothing
worth saying simply doesn't appear.

| Beat | Scope |
|---|---|
| AI & tech industry | Model releases, agent tooling, the business and policy fights around them |
| Macro & markets | Fed path, inflation, employment, market-moving earnings |
| World economy | US, EU, China, Middle East — **especially US policy toward and interaction with each** |
| US financials | Top US banks, asset managers, payments. JPMorgan and its direct competitors get standing attention |
| US politics & policy | Legislation, courts, regulation. Substance only |
| Geopolitics | Conflicts and rivalries with real second-order consequences |
| Science & public health | Research that changes how something works |
| UAP disclosure | Government disclosure, credible releases, new imagery from state or public sources. Lumpy cadence — appears when something real happens |
| *Wildcard* | **Unset — tell the skill what this is** |

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
| Ukraine–Russia negotiations | active | Whether anything survives the 8 Sep expiry of the reciprocal capital-strike pause; a text either side will describe; a front-line ceasefire beyond the two capitals. Not commentary — Peskov declined on 7 Sep to say how the Witkoff proposals differ from Anchorage. | 2026-09-06 (no movement 7 Sep) |
| Hormuz closure & EU energy response | active | Whether Iran publishes coordinates for the "restricted zone" announced 7 Sep; whether the Iran–Oman corridor is actually signed and whether Muscat confirms; daily Hormuz transit counts holding in single digits off the ~10/day Kpler average; SPR level below 290 mb; EU price-cap decision | 2026-09-07 |
| Gulf states & Article 51 | active | Kuwait or the UAE restricting US use of the bases struck; a collective GCC statement rather than individual condemnations | 2026-09-05 |
| Fed September decision | active | 11 Sep CPI print; 16 Sep FOMC statement. Post-Aug-payrolls the live question is a hike, not the size of a cut. | 2026-09-06 |
| US fuel prices | active | The 8 Sep EIA weekly print, the first official reading that can contain the alleged $5.85 record; distillate stock builds | 2026-09-05 |
| Missouri congressional map | active | An order from Justice Kavanaugh alone or a referral to the full Court; the state-law ballot-change cutoff this week (sources give 8 or 9 Sep); the 19 Sep overseas-ballot mailing date; the state's requested 14 Sep resolution date; ballot-access or residency litigation over nominees from the voided primaries | 2026-09-07 |
| Autonomous weapons regulation | active | CCW Seventh Review Conference, 16–20 Nov 2026: negotiate / extend / lapse. Publication of the agreed definition text. Corroboration of the "diluted in the final hours" claim from a newsroom other than Reuters. | 2026-09-06 (new) |
| Indonesia free-meals programme (MBG) | active | Lab results identifying the pathogen; suspension of distribution in affected provinces; any change to the 2027 budget line | 2026-09-06 (new) |
| Anak Krakatau | active | Movement off alert level III in either direction; Jakarta schools reopening; ash affecting cruise-altitude airways rather than terminal airspace; any tsunami advisory | 2026-09-07 |
| USPS mail ballot rule | active | Supreme Court order on application No. 26A297. Responses due 10am 8 Sep per Justice Jackson; TRO expiry 10 Sep | — (no movement 2026-09-06) |
| Birthright citizenship order | active | Appeal filed to the Fourth Circuit, or emergency application to SCOTUS | — (no movement 2026-09-06) |
| AI gated-capability tiers | active | Published tier criteria or an access list for GPT-6 Astra's restricted cyber capabilities, or a regulator demanding them | 2026-09-05 |
| UAP disclosure implementation | active | ODNI's detailed implementing guidance, and whether it closes the contractor gap left by the 31 Jul preliminary guidance. House Oversight task force hearing 9 Sep. | 2026-09-05 |
| AARO records contract | active | Award notice on sam.gov, or a public tranche drawing on the NUFOHRC collection | — (no movement 2026-09-06) |
| Central bank gold custody | active | Another central bank discloses relocation, or Bundesbank / Banca d'Italia comment | — (no movement 2026-09-06) |
| Bank stablecoin consortium | active | JPMorgan statement; first GENIUS Act licence; consortium entity formation; OCC final rules targeted Nov 2026 | — (no movement 2026-09-06) |
| Tampa Bay dengue | active | The week-35 arbovirus report (not published/reachable as of 6 Sep): whether Pasco stays at one case, and the regional trend line past 65 | 2026-09-05 |
| Florida Amendment 3 | active | Publication of the AG's revised ballot title and summary; county-level revenue estimates for Pasco and Pinellas. State declined to appeal on 7 Aug — not a trigger. | 2026-09-05 |
| Waymo Tampa Bay | active | Service-area expansion into Pinellas or Pasco, or published incident data | — (no movement 2026-09-07) |
| Saxony-Anhalt government formation | active | A Minister-President vote in the Landtag; a coalition agreement; fresh elections. AfD holds 39 of 83, majority is 42. | 2026-09-07 (new) |
| Miami 767 overrun (21 Air / Amazon) | active | NTSB preliminary report or flight-recorder readout; FAA action against 21 Air's certificate; any finding on the runway safety area at MIA runway 30 | 2026-09-07 (new) |
| Nepal–Tibet glacial flood & Loss and Damage | active | A Loss and Damage Fund board decision on Nepal's claim, and at what figure; the search being called off; the ~5,000 missing being converted to presumed dead; whether the UN's $50m appeal is funded | 2026-09-07 (new) |
| Israel–Lebanon June framework | active | Formal abandonment of the framework; an Israeli withdrawal from a pilot zone; Hezbollah action beyond drone launches; a UN or ICRC response to the 135 healthcare-worker deaths | 2026-09-07 (new) |
| EU–Greenland partnership | active | A US response to the 7 Sep Nuuk signing; whether the €530m survives the 2028–34 MFF negotiation; any actual critical-minerals project reaching a decision | 2026-09-07 (new) |
| Florida school vaccine rule | active | Close of comment ~14 Sep; whether a public hearing is granted; adoption as drafted; any legal challenge. The broadened "moral or ethical" exemption applies to the statutory measles and polio requirements too. | 2026-09-07 (new) |
| Florida emergency management funding | active | Joint Legislative Budget Commission action on the $250m request; accounting for the ~70% of FY26-27 budget already spent; any storm landfall that tests it | 2026-09-07 (new) |
| JLR restructuring & European autos | active | Close of the voluntary redundancy window 4 Oct; compulsory notices; outcome of the Reynolds meeting; whether cash break-even actually reaches 300,000 units by FY27; any reprofiling of the £15–18bn investment line | 2026-09-07 (new) |
| Acton attack prosecution | active | Tuesday 8 Sep arraignment and whether the two felony assault counts survive it; any charge added relating to the weapons or to Acton herself; the Ohio State Highway Patrol threat assessment; a change in candidate security posture before November | 2026-09-07 (new) |

*Dormancy note: the 6-month dormancy clock has not expired for any thread — this watchlist opened 5 September 2026. "No movement" means swept and no trigger fired.*
