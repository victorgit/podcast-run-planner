/**
 * User profile component showing logged-in user info.
 */

import Button from '../ui/Button';
import { useAuth } from '../../hooks/useAuth';

export default function UserProfile() {
  const { user, logout } = useAuth();

  if (!user) {
    return null;
  }

  return (
    <div className="bg-white rounded-lg shadow-md p-6 mb-6">
      <div className="flex items-center justify-between">
        <div className="flex items-center space-x-4">
          {user.images && user.images.length > 0 && (
            <img
              src={user.images[0].url}
              alt={user.display_name || 'User'}
              className="w-12 h-12 rounded-full"
            />
          )}
          <div>
            <h3 className="text-lg font-semibold text-gray-900">
              {user.display_name || 'User'}
            </h3>
            {user.email && (
              <p className="text-sm text-gray-600">{user.email}</p>
            )}
          </div>
        </div>
        <Button onClick={logout} variant="secondary">
          Logout
        </Button>
      </div>
    </div>
  );
}

