import logging
from ldap3 import Server, Connection, ALL
from ldap3.core import exceptions

from base import errors


class LdapCli:

    def __init__(self, host, root_dn, username, password):
        self.host = host
        self.username = username
        self.password = password
        self.root_dn = root_dn
        self.group_dn = f'cn=group,{self.root_dn}'
        self.member_dn = f'cn=member,{self.root_dn}'
        self.server = Server(self.host)

    def _create_connection(self):
        return Connection(self.server, f'cn={self.username},{self.root_dn}', self.password, auto_bind=True)

    def get_users(self):
        '''
        获取用户列表
        '''
        dn = 'cn=member,dc=waylonglong,dc=com'
        conn = self._create_connection()
        attributes = ['cn', 'sn']
        conn.search(dn, '(objectclass=person)', attributes=attributes)
        data_list = []
        for user in conn.entries:
            user = user.entry_attributes_as_dict
            data = {
                'username': user['cn'][0],
                'name': user['sn'][0],
            }
            data_list.append(data)
        return data_list

    def check_password(self, username, password):
        '''
        校验密码
        '''
        dn = f'cn={username},cn=member,dc=waylonglong,dc=com'
        try:
            Connection(self.server, dn, password, auto_bind=True)
        except exceptions.LDAPBindError as e:
            return False
        return True


ldap_cli = LdapCli('ldap://127.0.0.1:389', 'dc=waylonglong,dc=com', 'admin', 'ldap123')
