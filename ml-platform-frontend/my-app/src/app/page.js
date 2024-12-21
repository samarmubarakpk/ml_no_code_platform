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
    <main className="p-8">
      <h1 className="text-2xl font-bold mb-4">ML Platform Prototype</h1>
      
      <div className="space-y-4">
        <div>
          <label>Training Set (%): </label>
          <input 
            type="number" 
            value={trainSize} 
            onChange={(e) => setTrainSize(Number(e.target.value))}
            className="border p-1"
          />
        </div>

        <div>
          <label>Validation Set (%): </label>
          <input 
            type="number" 
            value={valSize} 
            onChange={(e) => setValSize(Number(e.target.value))}
            className="border p-1"
          />
        </div>

        <button 
          onClick={handleSplit}
          className="bg-blue-500 text-white px-4 py-2 rounded"
        >
          Split Data
        </button>

        {splitSizes && (
          <div className="mt-4">
            <h2 className="text-xl font-bold">Results:</h2>
            <p>Training Set: {splitSizes.train_size} samples</p>
            <p>Validation Set: {splitSizes.val_size} samples</p>
            <p>Test Set: {splitSizes.test_size} samples</p>
          </div>
        )}
      </div>
    </main>
  )
}