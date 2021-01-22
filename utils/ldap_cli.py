import logging
from ldap3 import Server, Connection, ALL
from ldap3.core import exceptions

from base import errors


class LdapCli:

    def __init__(self, host, root_dn, username, password):
        self.host = host
        self.root_dn = root_dn
        self.group_dn = f'cn=group,{self.root_dn}'
        self.member_dn = f'cn=member,{self.root_dn}'
        self.server = Server(self.host)
        self.conn = Connection(self.server, f'cn={username},{self.root_dn}', password, auto_bind=True)

    def _gen_password(self):
        return '123456'

    def add_user(self, username, name):
        '''
        返回True为成功、False为失败
        '''
        dn = f'cn={username},{self.member_dn}'
        object_class = 'inetOrgPerson'
        attribute = {
            'sn': f'{name}',
            'uid': f'{username}',
            'userPassword': self._gen_password(),
        }
        return self.conn.add(dn, object_class, attribute)


ldap_cli = LdapCli('ldap://127.0.0.1:389', 'dc=waylonglong,dc=com', 'admin', 'ldap123')
