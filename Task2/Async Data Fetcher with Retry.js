/**
 * A small mock network request used for testing retry behavior.
 * Randomly succeeds or fails to mimic unstable networks.
 */
function mockFetch(url) {
  console.log(`Fetching: ${url}`);

  return new Promise((resolve, reject) => {
    setTimeout(() => {
      const ok = Math.random() > 0.4; // roughly 60% success rate
      if (ok) {
        console.log("✔ Request succeeded");
        resolve(`Response from ${url}`);
      } else {
        console.log("✖ Request failed (simulated)");
        reject(new Error(`Could not fetch ${url}`));
      }
    }, 300);
  });
}

/**
 * Attempts to fetch data from a URL, retrying a few times if it fails.
 *
 * @param {string} url - Target URL or resource name.
 * @param {number} maxRetries - How many times to retry after the first failure.
 * @returns {Promise<string>}
 */
async function fetchDataWithRetry(url, maxRetries) {
  const sleep = (ms) => new Promise((res) => setTimeout(res, ms));

  let error = null;

  for (let attempt = 1; attempt <= maxRetries + 1; attempt++) {
    try {
      const result = await mockFetch(url);
      return result;
    } catch (err) {
      error = err;

      const retriesLeft = maxRetries - (attempt - 1);
      console.warn(`Attempt ${attempt} failed. Remaining retries: ${retriesLeft}`);

      if (attempt === maxRetries + 1) {
        throw new Error(
          `All ${maxRetries} retries failed. Last error: ${error.message}`
        );
      }

      console.log(`Retrying in 1 second...`);
      await sleep(1000);
    }
  }
}

/* ------------------------  Example Usage  ------------------------ */

async function runDemo() {
  console.log("---- Example 1: Mock Fetch with Retry ----");

  try {
    const data = await fetchDataWithRetry("Sample-Resource", 3);
    console.log("Final Result:", data);
  } catch (err) {
    console.log("Final Error:", err.message);
  }

  console.log("\n---- Example 2: Real URL Fetch (no mock) ----");

  try {
    const realUrl = "https://jsonplaceholder.typicode.com/todos/1";
    const response = await fetch(realUrl);
    const jsonData = await response.json();
    console.log("Fetched real API data:", jsonData);
  } catch (err) {
    console.error("Failed to fetch real data:", err.message);
  }
}

runDemo();
