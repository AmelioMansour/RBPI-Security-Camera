import "./App.css";

function App() {
    return (
        <div className="App">
          <h1>Security Camera</h1>
          <p>CSI4160</p>
            <video src="https://storage.googleapis.com/security_videos_csi4160/Security%2014-11-2023-22-56-30.mp4" controls></video>
        </div>
    );
}

export default App;