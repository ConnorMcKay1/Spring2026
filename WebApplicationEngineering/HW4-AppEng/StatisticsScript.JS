
const { useState } = React;

  // input compoenent
function InputField({ value, setValue }) {
  return (
    <input
      className="form-control"
      value={value}
      onChange={(e) => setValue(e.target.value)}
      placeholder="e.g. 1,2,3,4"
    />
  );
}

// the result component
function Results({ numbers, show }) {

  if (!show) return null;

  // checker for the input being >= 2, for obvious reasons
  if (numbers.length < 2) {
    return <div className="text-danger mt-2">
      Please enter at least 2 valid numbers.
    </div>;
  }

  const mean =
    numbers.reduce((a, b) => a + b, 0) / numbers.length;

  const variance =
    numbers.reduce((acc, val) => acc + Math.pow(val - mean, 2), 0) /
    numbers.length;

  const stdDev = Math.sqrt(variance);

  //potential error with the sigma, still deploys
  // it just seems like VScode doesnt like it (other IDEs might?)
  return (
    <div className="mt-3">
      <div>Mean (μ): {mean.toFixed(2)}</div>
      <div>Std Dev (σ): {stdDev.toFixed(2)}</div>
    </div>
  );
}

// handles the logic such as comma seperate
// as well sa the check fro not a number
function App() {
  const [value, setValue] = useState("");
  const [submitted, setSubmitted] = useState(false);

  const numbers = value
    .split(",")
    .map(n => Number(n.trim()))
    .filter(n => !isNaN(n));

  function handleCalculate() {
    setSubmitted(true);
  }

  return (
    <div className="container mt-4">

      <InputField value={value} setValue={setValue} />

      <button
        className="btn btn-primary mt-2"
        onClick={handleCalculate}
      >
        Calculate
      </button>

      <Results numbers={numbers} show={submitted} />

    </div>
  );
}

// provides this as the react root
const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<App />);

