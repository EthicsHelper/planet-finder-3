import React, { useEffect, useState } from "react";
import { Canvas } from "@react-three/fiber";
import { OrbitControls, Sphere } from "@react-three/drei";
import * as THREE from "three";

export default function UniverseMapVω() {
  const [data, setData] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8080/data")
      .then((res) => res.json())
      .then((json) => setData(json));
  }, []);

  return (
    <div className="w-full h-screen bg-black text-white">
      <Canvas camera={{ position: [0, 0, 15], fov: 50 }}>
        <OrbitControls enableZoom={true} />
        <ambientLight intensity={0.5} />
        <pointLight position={[10, 10, 10]} />

        {data.map((p, i) => {
          const color = new THREE.Color(
            `hsl(${Math.min(120, p.P_life * 360)}, 100%, 50%)`
          );
          return (
            <Sphere key={i} args={[0.1, 16, 16]} position={[p.x / 1e6, p.y / 1e6, p.z / 1e6]}>
              <meshStandardMaterial color={color} emissive={color} emissiveIntensity={p.IELS} />
            </Sphere>
          );
        })}
      </Canvas>

      <div className="absolute top-4 left-4 text-sm bg-gray-900 bg-opacity-70 p-3 rounded-lg">
        <h2 className="text-lg font-bold">Life Finder Map (vΩ)</h2>
        <p>Each point represents a planet or moon segment.</p>
        <p>
          <span className="text-green-400">Green</span> = high Pₗᵢfₑ /
          <span className="text-yellow-400"> Yellow</span> = moderate /
          <span className="text-red-400"> Red</span> = low.
        </p>
      </div>
    </div>
  );
}
