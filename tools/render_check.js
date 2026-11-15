const { chromium } = require('playwright');
(async () => {
  const file = 'file://' + process.argv[2];
  const out  = process.argv[3];
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium', args:['--no-sandbox'] });
  const errs = [];
  for (const w of [380, 900]) {
    const pg = await b.newPage({ viewport: { width: w, height: 900 }, deviceScaleFactor: 1 });
    pg.on('console', m => { if (m.type() === 'error') errs.push(w + ': ' + m.text()); });
    pg.on('pageerror', e => errs.push(w + ': pageerror ' + e.message));
    await pg.goto(file, { waitUntil: 'load' });
    // open every <details> BEFORE measuring or screenshotting -- a figure inside
    // a collapsed <details> is invisible and the screenshot times out (14 Nov).
    await pg.evaluate(() => document.querySelectorAll('details').forEach(d => d.open = true));
    const m = await pg.evaluate(() => ({
      scrollW: document.documentElement.scrollWidth,
      clientW: document.documentElement.clientWidth,
      details: document.querySelectorAll('details').length,
      figs: document.querySelectorAll('figure svg').length,
      radios: document.querySelectorAll('.fb input[type=radio]').length,
      btn: !!document.getElementById('send-feedback'),
      ext: [...document.querySelectorAll('link[rel=stylesheet],script[src],img')].map(e => e.src || e.href),
    }));
    console.log(w + 'px: scrollWidth=' + m.scrollW + ' clientWidth=' + m.clientW +
                ' overflow=' + (m.scrollW > m.clientW + 1) + ' details=' + m.details +
                ' figureSvgs=' + m.figs + ' radios=' + m.radios + ' feedbackButton=' + m.btn +
                ' externalRefs=' + JSON.stringify(m.ext));
    await pg.screenshot({ path: out + '/render-' + w + '.png', fullPage: false });
    const fig = await pg.$('figure svg');
    if (fig) await fig.screenshot({ path: out + '/chart-' + w + '.png' });
    else console.log(w + 'px: NO FIGURE SVG FOUND');
    await pg.close();
  }
  console.log('console errors: ' + (errs.length ? JSON.stringify(errs) : 'none'));
  await b.close();
})();
