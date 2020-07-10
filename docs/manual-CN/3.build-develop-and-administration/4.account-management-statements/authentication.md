# Authentication

Whenever a client connects to **Nebula Graph**, a session is created. The session stores various contextual information about the connection. Each session is always associated with a single user.

Authentication is the process of mapping this session to a specific user. Once the session is mapped to a user, a set of permissions can be associated with it, using authorization.

**Nebula Graph** supports two authentication methods, explained in detail below - local and LDAP.

## Local Authentication

The local database stores usernames, encrypted passwords, local user settings and remote LDAP user settings. When a user tries to access the database, they will be met with a security challenge. If they can provide a valid username/password combination, a JWT token will be generated.

You need to enable the local authentication by setting the `--enable_authorize` property in the `nebula-graphd.conf` file (the directory is `/usr/local/nebula/etc/` by default) to `true`.

## LDAP Authentication

Lightweight Directory Access Protocol (LDAP) is a lightweight client-server protocol for accessing directory services. Users stored inside LDAP take precedence over the local database users. For example, if both providers have a user called “Amber”, the settings and roles for this user will be sourced from LDAP.

Unlike local authentication, besides enabling the `--enable_authorize` parameter, LDAP needs to be configured in the `nebula-graphd.conf` file (the directory is `/usr/local/nebula/etc/` by default). Refer to the [Integrating LDAP Document](TODO) for details.
