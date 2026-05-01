function App() {
  const [count, setCount] = React.useState(0);

  return (
    <div className="test-box">
      <h1>React is working 🎉</h1>
      <p>You clicked {count} times</p>

      <button
        className="btn btn-primary"
        onClick={() => setCount(count + 1)}
      >
        Click me
      </button>
    </div>
  );
}







const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<App />);