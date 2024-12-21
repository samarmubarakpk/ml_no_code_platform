// src/app/page.js
'use client'
import { useState } from 'react'

export default function Home() {
  const [splitSizes, setSplitSizes] = useState(null)
  const [trainSize, setTrainSize] = useState(70)
  const [valSize, setValSize] = useState(15)

  const handleSplit = async () => {
    try {
      const response = await fetch(
        `http://localhost:8000/split-data?train_size=${trainSize/100}&val_size=${valSize/100}`
      )
      const data = await response.json()
      setSplitSizes(data.split_sizes)
    } catch (error) {
      console.error('Error:', error)
    }
  }

  return (
    <main className="p-8 space-y-6">
      <h1 className="text-4xl font-extrabold mb-6">ML Platform Prototype</h1>

      <div className="grid grid-cols-1 sm:grid-cols-2 gap-6">
        <div>
          <label className="block text-lg font-medium mb-2">Training Set (%):</label>
          <input 
            type="number" 
            value={trainSize} 
            onChange={(e) => setTrainSize(Number(e.target.value))}
            className="w-full border rounded px-3 py-2 text-gray-700 focus:outline-none focus:ring focus:ring-blue-300"
          />
        </div>

        <div>
          <label className="block text-lg font-medium mb-2">Validation Set (%):</label>
          <input 
            type="number" 
            value={valSize} 
            onChange={(e) => setValSize(Number(e.target.value))}
            className="w-full border rounded px-3 py-2 text-gray-700 focus:outline-none focus:ring focus:ring-blue-300"
          />
        </div>
      </div>

      <button 
        onClick={handleSplit}
        className="w-full bg-blue-600 hover:bg-blue-700 text-white font-bold py-3 px-6 rounded transition duration-300"
      >
        Split Data
      </button>

      {splitSizes && (
        <div className="mt-6 bg-gray-100 p-4 rounded-lg shadow">
          <h2 className="text-2xl font-bold mb-4">Results:</h2>
          <ul className="space-y-2 text-lg">
            <li><strong>Training Set:</strong> {splitSizes.train_size} samples</li>
            <li><strong>Validation Set:</strong> {splitSizes.val_size} samples</li>
            <li><strong>Test Set:</strong> {splitSizes.test_size} samples</li>
          </ul>
        </div>
      )}
    </main>
  )
}
