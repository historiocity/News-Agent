# News-Agent

Justin's personalized daily news brief. The `news-brief` skill researches,
synthesizes, and publishes one self-contained HTML issue to `issues/` each morning,
served via GitHub Pages.

## What's here

```
News-Agent/
├── .github/workflows/daily-brief.yml   ← workflow_dispatch + late backstop crons
├── .claude/skills/news-brief/SKILL.md  ← the skill itself, vendored here
├── config.md                           ← beats, anti-topics, sources, watchlist
├── issues/YYYY-MM-DD.html              ← one issue per day, standalone
├── index.html                          ← archive, regenerated each run
└── .nojekyll                           ← serve files as-is
```

## Scheduling: read this before touching the crons

**A GitHub `schedule` cron cannot hit a wall-clock time, and this repo has the
measurements to prove it.** Scheduled workflows are not so much dropped as *queued
and delivered hours late*, and the delay is worst in the early-UTC morning —
precisely where a 5am America/New_York target lives.

Measured 8–14 September 2026: a `7 9 * * *` cron (09:07 UTC, 5:07am EDT) produced a
run on the intended morning **zero times in seven days**. On 13 September the four
slots 09:07, 10:41, 13:29 and 22:11 UTC came out at 13:46, 14:17, 14:39, 17:00 and
00:06 the following day; the 09:07 slot produced nothing at all.

That failure was invisible for a week because the late runs all stand down correctly
in ~10 seconds once the day's issue exists. The gate works. The clock does not.

So the crons in this workflow are **backstops only**, deliberately late, and
`workflow_dispatch` is the primary path — dispatches start within seconds.

**Do not re-add a "5am" cron.** It will look like a safety net and will not be one,
and its presence is what made this schedule appear to work for a week.

### Making 5am actually happen

The dispatch needs a caller that is awake at 5am. Nothing inside GitHub Actions or a
Claude session qualifies: Actions has only `schedule`, and a Claude Routine bound to a
session only runs when that session next wakes (measured: fired 09:02 UTC, processed
13 hours later). An external scheduler is the only thing that works.

1. Create a **fine-grained** personal access token, scoped to this repository only,
   with exactly one permission: **Actions → Read and write**. Nothing else. Set an
   expiry and a reminder to rotate it.
2. Point any always-on scheduler at the dispatch endpoint once a day at 5am local —
   cron-job.org, EasyCron, a Cloudflare Worker with a Cron Trigger, or a shortcut on
   a machine that stays on overnight:

   ```sh
   curl -X POST \
     -H "Authorization: Bearer $GH_PAT" \
     -H "Accept: application/vnd.github+json" \
     https://api.github.com/repos/historiocity/News-Agent/actions/workflows/daily-brief.yml/dispatches \
     -d '{"ref":"main"}'
   ```

Firing this blindly is safe: the workflow's gate refuses to write a second issue for
a local day that already has one, so a duplicate dispatch cannot double-post.

If you skip this, the backstop crons still deliver unattended — just between roughly
6:45am and noon local rather than at 5am.

## Relationship to claude-skills

The operative copy of the skill is **vendored in this repo** at
`.claude/skills/news-brief/SKILL.md`, so scheduled runs and interactive sessions in
this checkout read the same file. An earlier design had the workflow download the
skill from `claude-skills` at run time *over the top of* the vendored copy, which
meant two copies fighting and repeated manual syncing; that download step was removed.

The canonical copy still lives in
[`historiocity/claude-skills`](https://github.com/historiocity/claude-skills) under
`plugins/global-skills/skills/news-brief/`, and the two are kept in step by hand when
the skill changes. That copy is what makes the skill available interactively anywhere
the marketplace plugin is installed:

```sh
/plugin marketplace add historiocity/claude-skills
/plugin install global-skills@jd-skills
```

Ask for a brief on any device and you get one immediately, with no repo involved.
This repo is what adds the archive, the persistent watchlist, and the feedback loop.

## Setup

Full instructions live with the skill, at
`plugins/global-skills/skills/news-brief/references/repo-setup.md`. The short version:

1. `claude setup-token` locally, then add the result as the repo secret
   `CLAUDE_CODE_OAUTH_TOKEN` (Settings → Secrets and variables → Actions). Runs bill
   to the Claude subscription rather than the API.
2. Install the Claude GitHub App on this repo: https://github.com/apps/claude
3. Settings → Pages → deploy from `main`, root. **Pages paths are case-sensitive:**
   the URL is `historiocity.github.io/News-Agent/`, and the lowercase form 404s.
4. Actions tab → Daily Brief → Run workflow, to produce issue one.
5. Optionally, the external 5am scheduler above.

The `brief-ready`, `brief-feedback` and `brief-failed` labels are created by the
workflow itself, so there is nothing to do by hand. (`brief-feedback` in particular
must exist: the in-issue feedback button links to `issues/new?labels=brief-feedback`,
and GitHub *silently drops* labels that do not exist, which lost a week of reader
feedback before the workflow started creating it.)

## Feedback

Each issue has radio controls per lead story, and one question about the "Also today"
tier as a whole. Answering them and hitting the button at the bottom opens a prefilled
GitHub issue labeled `brief-feedback`. The next morning's run reads open feedback
issues, folds them into `config.md`, and closes them with a note saying what changed.

## A note on visibility

This repo is public, which is what makes free GitHub Pages hosting work. That means
`config.md` and every feedback issue are world-readable. `config.md` describes the
reader; feedback issues record reactions to specific stories. Keep anything that
shouldn't be indexed out of both.
