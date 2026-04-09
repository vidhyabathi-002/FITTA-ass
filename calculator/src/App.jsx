import { useState } from 'react'
import './App.css'

function App() {
  const [num1, setNum1] = useState('');
  const [num2, setNum2] = useState('');
  const [result, setResult] = useState(null);

  const handleAdd = () => {
    const sum = parseFloat(num1) + parseFloat(num2);
    setResult(sum);
  };

  return (
    <div style={{ textAlign: 'center', marginTop: '50px' }}>
      <h1>Simple Calculator</h1>
      <input 
        type="number" 
        value={num1} 
        onChange={(e) => setNum1(e.target.value)} 
        placeholder="Enter first number" 
        style={{ margin: '10px', padding: '10px' }}
      />
      <input 
        type="number" 
        value={num2} 
        onChange={(e) => setNum2(e.target.value)} 
        placeholder="Enter second number" 
        style={{ margin: '10px', padding: '10px' }}
      />
      <br />
      <button 
        onClick={handleAdd} 
        style={{ margin: '10px', padding: '10px 20px' }}
      >
        Add
      </button>
      {result !== null && <p style={{ fontSize: '20px' }}>Result: {result}</p>}
    </div>
  )
}

export default App
