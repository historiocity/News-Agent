# News-Agent

Justin's personalized daily news brief. A scheduled GitHub Action runs the
`news-brief` skill each morning, which researches, synthesizes, and publishes one
self-contained HTML issue to `issues/`, served via GitHub Pages.

## What's here

```
News-Agent/
├── .github/workflows/daily-brief.yml   ← cron 08:00 UTC (4am EDT / 3am EST)
├── config.md                           ← beats, anti-topics, sources, watchlist
├── issues/YYYY-MM-DD.html              ← one issue per day, standalone
├── index.html                          ← archive, regenerated each run
└── .nojekyll                           ← serve files as-is
```

## Relationship to claude-skills

The skill itself is **not** in this repo. It lives in
[`historiocity/claude-skills`](https://github.com/historiocity/claude-skills) under
`plugins/global-skills/skills/news-brief/`, and the workflow checks that repo out at
run time and stages it onto the runner. One copy, no drift.

That also means the skill is available interactively anywhere the marketplace plugin
is installed:

```sh
/plugin marketplace add historiocity/claude-skills
/plugin install global-skills@jd-skills
```

Ask for a brief on any device and you get one immediately, with no repo involved.
This repo is what adds the archive, the persistent watchlist, the feedback loop, and
the 4am cron.

## Setup

Full instructions live with the skill, at
`plugins/global-skills/skills/news-brief/references/repo-setup.md`. The short version:

1. `claude setup-token` locally, then add the result as the repo secret
   `CLAUDE_CODE_OAUTH_TOKEN` (Settings → Secrets and variables → Actions). Runs bill
   to the Claude subscription rather than the API.
2. Install the Claude GitHub App on this repo: https://github.com/apps/claude
3. Create the feedback label:
   `gh label create brief-feedback --description "Reader response to a brief issue" --color 0E8A16`
4. Settings → Pages → deploy from `main`, root.
5. Actions tab → Daily Brief → Run workflow, to produce issue one without waiting for
   cron.

## Feedback

Each issue has radio controls per story. Answering them and hitting the button at the
bottom opens a prefilled GitHub issue labeled `brief-feedback`. The next morning's run
reads open feedback issues, folds them into `config.md`, and closes them with a note
saying what changed.

## A note on visibility

This repo is public, which is what makes free GitHub Pages hosting work. That means
`config.md` and every feedback issue are world-readable. `config.md` describes the
reader; feedback issues record reactions to specific stories. Keep anything that
shouldn't be indexed out of both.
