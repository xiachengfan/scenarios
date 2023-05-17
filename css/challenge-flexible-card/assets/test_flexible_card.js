const puppeteer = require("puppeteer");
try {
  (async () => {
    const browser = await puppeteer.launch({
      args: ["--no-sandbox", "--disable-setuid-sandbox"],
      //headless: false
    });
    const page = await browser.newPage();
    await page.setViewport({ width: 1200, height: 750 });
    /*await page.goto("http://127.0.0.1:8080/flexible_card.html", {
            waitUntil: "networkidle0",
        });*/
    /* Check whether the port is available */
    try {
      await page.goto("http://127.0.0.1:8080/flexible_card.html");
      console.log("Port 8080 is enabled!");
    } catch (error) {
      console.log("Port 8080 is not enabled.");
      process.exit(1);
    }
    /* Detects whether the section element contains flex attributes */
    const elem1 = await page.$("section");
    const val1 = await page.evaluate((x) => {
      return JSON.parse(JSON.stringify(window.getComputedStyle(x)));
    }, elem1);
    console.log(val1);
    console.log(val1.display);
    console.log(val1.flexWrap);
    console.log(val1.justifyContent);
    if (
      val1.display == "flex" &&
      val1.flexWrap == "wrap" &&
      val1.justifyContent == "space-between"
    ) {
      console.log("Congratulations! you are passed.");
    } else {
      console.error("Sorry! you didn't pass the challenge.");
      process.exit(1);
    }

    await browser.close();
  })();
} catch (err) {
  console.log(err);
}
