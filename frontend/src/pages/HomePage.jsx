/**
 * Home/Landing page.
 */

import { useEffect, useState } from 'react';
import LoginButton from '../components/features/LoginButton';
import UserProfile from '../components/features/UserProfile';
import { useAuth } from '../hooks/useAuth';

export default function HomePage() {
  const { user, loading, isAuthenticated } = useAuth();
  const [loginStatus, setLoginStatus] = useState(null);

  useEffect(() => {
    // Check URL params for login status
    const params = new URLSearchParams(window.location.search);
    const loginParam = params.get('login');
    const errorParam = params.get('error');

    if (loginParam === 'success') {
      setLoginStatus('success');
      // Clear URL params
      window.history.replaceState({}, document.title, window.location.pathname);
      // Refresh auth state
      setTimeout(() => window.location.reload(), 500);
    } else if (errorParam) {
      setLoginStatus('error');
      // Clear URL params
      window.history.replaceState({}, document.title, window.location.pathname);
    }
  }, []);

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
          {/* Show login status messages */}
          {loginStatus === 'success' && (
            <div className="mb-4 p-4 bg-green-50 border border-green-200 rounded-lg">
              <p className="text-green-800">Successfully logged in!</p>
            </div>
          )}
          {loginStatus === 'error' && (
            <div className="mb-4 p-4 bg-red-50 border border-red-200 rounded-lg">
              <p className="text-red-800">
                Login failed. Please try again.
              </p>
            </div>
          )}

          {/* Show user profile if logged in */}
          {!loading && isAuthenticated && <UserProfile />}

          <div className="bg-white rounded-lg shadow-md p-8">
            {loading ? (
              <div className="text-center py-8">
                <p className="text-gray-600">Loading...</p>
              </div>
            ) : isAuthenticated ? (
              <>
                <h2 className="text-2xl font-semibold mb-4">Welcome back!</h2>
                <p className="text-gray-700 mb-6">
                  You're logged in and ready to plan your next run. The playlist
                  generation feature will be available soon.
                </p>
                <div className="space-y-4">
                  <div className="p-4 bg-blue-50 rounded-lg">
                    <h3 className="font-semibold text-blue-900 mb-2">
                      Coming Soon
                    </h3>
                    <ul className="list-disc list-inside text-blue-800 space-y-1">
                      <li>Run planning form</li>
                      <li>Playlist generation</li>
                      <li>Save to Spotify</li>
                    </ul>
                  </div>
                </div>
              </>
            ) : (
              <>
                <h2 className="text-2xl font-semibold mb-4">Welcome</h2>
                <p className="text-gray-700 mb-6">
                  This is the Podcast Run Planner MVP. The app will help you
                  create Spotify playlists tailored to your run duration and
                  preferences.
                </p>

                <div className="mt-8">
                  <LoginButton />
                </div>
              </>
            )}
          </div>
        </main>
      </div>
    </div>
  );
}
