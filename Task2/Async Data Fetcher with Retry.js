/**
 * Mock API call function that randomly succeeds or fails.
 * @returns {Promise<string>} Resolves with data or rejects with an error.
 */
function mockFetch(url) {
  console.log(`Attempting to fetch data from: ${url}`);
  return new Promise((resolve, reject) => {
    // Simulate network delay
    setTimeout(() => {
      const success = Math.random() > 0.4; // 60% chance of success
      if (success) {
        console.log("-> Success!");
        resolve(`Data for ${url}`);
      } else {
        console.log("-> Failure (Simulated network error)");
        reject(new Error(`Fetch failed for ${url}`));
      }
    }, 300); // Small delay to simulate latency
  });
}

/**
 * Fetches data from a URL with a specified number of retries upon failure.
 * Waits 1 second between retries.
 * * @param {string} url The URL (or mock function label) to fetch from.
 * @param {number} maxRetries The maximum number of times to retry on failure.
 * @returns {Promise<string>} The fetched data.
 * @throws {Error} Throws an error if all retries fail.
 */
async function fetchDataWithRetry(url, maxRetries) {
  // Helper function to pause execution for a given duration
  const delay = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

  let lastError = null;

  // Loop iterates maxRetries + 1 (the initial attempt plus all retries)
  for (let attempt = 1; attempt <= maxRetries + 1; attempt++) {
    try {
      // Attempt the fetch
      const data = await mockFetch(url);
      // If successful, return the data immediately
      return data;
    } catch (error) {
      lastError = error;
      console.warn(
        `Attempt ${attempt} failed. Retries left: ${maxRetries - (attempt - 1)}`
      );

      // Check if this was the last possible attempt (maxRetries + 1)
      if (attempt === maxRetries + 1) {
        console.error(
          `Max retries reached (${maxRetries}). Throwing final error.`
        );
        // If max retries are reached, throw the error
        throw new Error(
          `Failed to fetch data after ${maxRetries} retries. Reason: ${lastError.message}`
        );
      }

      // Wait 1 second before the next attempt
      console.log(`Waiting 1 second before attempt ${attempt + 1}...`);
      await delay(1000);
    }
  }
}

// --- Working Examples ---
async function runExamples() {
  console.log(
    "--- Example 1: Successful Fetch (should succeed quickly or after a few retries) ---"
  );
  try {
    const result = await fetchDataWithRetry("Resource-A", 3);
    console.log(`\nExample 1 Final Result: ${result}\n`);
  } catch (e) {
    console.error(`\nExample 1 Final Failure: ${e.message}\n`);
  }

  console.log("--- Example 2: Maximum Retries Scenario (likely to fail) ---");
  // Using a higher chance of failure (e.g., if we modified mockFetch to 90% fail rate)
  // to reliably test the max retry path. Keeping the original 60% success rate
  // makes this a good real-world test of the retry mechanism.
  try {
    const result = await fetchDataWithRetry("Resource-B", 2);
    console.log(`\nExample 2 Final Result: ${result}\n`);
  } catch (e) {
    console.error(`\nExample 2 Final Failure: ${e.message}\n`);
  }
}

runExamples();
