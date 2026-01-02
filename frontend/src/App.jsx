import { useState, useEffect } from "react";
import { fetchTrafficData } from "./api";

function App() {
  const REFRESH_INTERVAL = 12;

  const [trafficData, setTrafficData] = useState(null);
  const [error, setError] = useState(null);
  const [countdown, setCountdown] = useState(REFRESH_INTERVAL);

  useEffect(() => {
    // Initial load
    fetchTrafficData()
      .then(setTrafficData)
      .catch((err) => setError(err.message));

    const interval = setInterval(() => {
      setCountdown((prev) => {
        if (prev === 1) {
          fetchTrafficData()
            .then(setTrafficData)
            .catch((err) => setError(err.message));

          return REFRESH_INTERVAL;
        }
        return prev - 1;
      });
    }, 1000);

    return () => clearInterval(interval);
  }, []);

  if (error) {
    return (
      <div className="min-h-screen flex items-center justify-center text-red-600">
        Error: {error}
      </div>
    );
  }

  if (!trafficData) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        Loading Traffic Data...
      </div>
    );
  }

  // 🔹 Find highest density
  const densities = trafficData.roads.map((r) => r.density_score);
  const maxDensity = Math.max(...densities);

  return (
    <div className="min-h-screen bg-gray-100 p-6">
      <h1 className="text-3xl font-bold m-1 ">Real-Time Traffic Dashboard</h1>

      {/* Countdown */}
      <div className=" flex justify-center">
        <div className="text-lg font-semibold text-green-700 bg-green-100 px-4 rounded-full">
          Next traffic update in{" "}
          <span className="font-bold text-green-900">{countdown}</span> seconds
        </div>
      </div>

      {/* Latency */}
      <div className="mb-3 text-sm text-gray-600">
        Backend Processing: {trafficData.processing_time_ms} ms | Frontend
        Latency: {trafficData.frontend_latency_ms} ms
      </div>

      {/* Roads */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        {trafficData.roads.map((road) => {
          const isGreen = road.density_score === maxDensity;

          return (
            <div key={road.road_id} className="bg-white p-4 rounded shadow">
              <div className="flex items-center gap-3">
                <h2 className="text-xl font-semibold">{road.road_id}</h2>

                <div className="flex items-center gap-1">
                  {(isGreen ? [1, 2, 3] : [1]).map((_, idx) => (
                    <div
                      key={idx}
                      className={`w-3.5 h-3.5 rounded-full ${
                        isGreen ? "bg-green-500" : "bg-red-500"
                      }`}
                    ></div>
                  ))}
                </div>
              </div>

              <p>
                Traffic Level: <b>{road.traffic_level}</b>
              </p>

              <p>Green Time: {road.green_time_sec} sec</p>

              <img
                src={road.image_url}
                alt={`Traffic view for ${road.road_id}`}
                className="w-full h-40 object-cover rounded mt-2"
              />
            </div>
          );
        })}
      </div>
    </div>
  );
}

export default App;
