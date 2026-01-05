/**
 * Custom hook for authentication state management.
 */

import { useState, useEffect } from 'react';
import { auth } from '../lib/api';

export function useAuth() {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    checkAuth();
  }, []);

  const checkAuth = async () => {
    try {
      setLoading(true);
      const userData = await auth.getCurrentUser();
      setUser(userData);
      setError(null);
    } catch (err) {
      // Not authenticated or error
      setUser(null);
      setError(null); // Don't show error for "not logged in"
    } finally {
      setLoading(false);
    }
  };

  const logout = async () => {
    try {
      await auth.logout();
      setUser(null);
      // Reload page to clear any cached state
      window.location.href = '/';
    } catch (err) {
      console.error('Logout error:', err);
    }
  };

  return {
    user,
    loading,
    error,
    isAuthenticated: !!user,
    checkAuth,
    logout,
  };
}

