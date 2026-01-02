const BACKEND_URL = "http://127.0.0.1:8000";

export async function fetchTrafficData() {
  const startTime = performance.now();
  const response = await fetch(`${BACKEND_URL}/analyze-traffic`);
  if (!response.ok) {
    throw new Error("Failed to fetch traffic data");
  }
  const data = await response.json();
  const endTime = performance.now();
  const frontendLatency = Math.round(endTime - startTime);
  return {
    ...data,
    frontend_latency_ms: frontendLatency,
  };
}
