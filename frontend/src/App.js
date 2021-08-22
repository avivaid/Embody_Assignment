import './App.css';
import AudioPlayer from 'material-ui-audio-player';


function App() {
  return (
    <div className="App">
      <header className="App-header">

  <AudioPlayer
    elevation={1}
    width="100%"
    variation="default"
    spacing={3}
    download={true}
    autoplay={true}
    order="standart"
    preload="auto"
    loop={true}
    src={'./assets/song.mp3'}
  />
      </header>
   
    </div>
  );
}

export default App;
