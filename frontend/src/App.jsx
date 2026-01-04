
function App() {
  return (
    <div className="min-h-screen bg-gray-50">
      <div className="container mx-auto px-4 py-8">
        <header className="text-center mb-12">
          <h1 className="text-4xl font-bold text-gray-900 mb-2">
            Podcast Run Planner
          </h1>
          <p className="text-gray-600">
            Generate perfect podcast playlists for your runs
          </p>
        </header>

        <main className="max-w-2xl mx-auto">
          <div className="bg-white rounded-lg shadow-md p-8">
            <h2 className="text-2xl font-semibold mb-4">Welcome</h2>
            <p className="text-gray-700 mb-6">
              This is the Podcast Run Planner MVP. The app will help you create
              Spotify playlists tailored to your run duration and preferences.
            </p>
            <div className="space-y-4">
              <div className="p-4 bg-blue-50 rounded-lg">
                <h3 className="font-semibold text-blue-900 mb-2">
                  Coming Soon
                </h3>
                <ul className="list-disc list-inside text-blue-800 space-y-1">
                  <li>Spotify OAuth login</li>
                  <li>Run planning form</li>
                  <li>Playlist generation</li>
                  <li>Save to Spotify</li>
                </ul>
              </div>
            </div>
          </div>
        </main>
      </div>
    </div>
  )
}

export default App
