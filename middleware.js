// Basic Authentication Middleware for Vercel Edge
export const config = {
  matcher: ['/((?!_next/static|_next/image|favicon.ico).*)'],
}

function parseBasicAuth(authHeader) {
  if (!authHeader || !authHeader.startsWith('Basic ')) {
    return null
  }

  try {
    const base64Credentials = authHeader.substring(6)
    const credentials = Buffer.from(base64Credentials, 'base64').toString('utf8')
    const [username, password] = credentials.split(':')
    return { username, password }
  } catch {
    return null
  }
}

export default function middleware(request) {
  const authHeader = request.headers.get('authorization')

  if (!authHeader) {
    return new Response('Authentication required', {
      status: 401,
      headers: {
        'WWW-Authenticate': 'Basic realm="RedPeak Intelligence Portal"',
      },
    })
  }

  const credentials = parseBasicAuth(authHeader)

  if (!credentials || credentials.username !== 'client' || credentials.password !== 'RedPeak101!') {
    return new Response('Invalid credentials', {
      status: 401,
      headers: {
        'WWW-Authenticate': 'Basic realm="RedPeak Intelligence Portal"',
      },
    })
  }

  return null // Allow request to continue
}
