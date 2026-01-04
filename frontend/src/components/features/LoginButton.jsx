/**
 * Login button component that redirects to Spotify OAuth.
 */

import Button from '../ui/Button';
import { auth } from '../../lib/api';

export default function LoginButton() {
  const handleLogin = () => {
    auth.login();
  };

  return (
    <Button onClick={handleLogin} variant="primary" className="w-full">
      Login with Spotify
    </Button>
  );
}

