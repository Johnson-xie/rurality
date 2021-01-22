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

    def _gen_password(self):
        return '123456'

    def _create_connection(self):
        return Connection(self.server, f'cn={self.username},{self.root_dn}', self.password, auto_bind=True)

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
        conn = self._create_connection()
        return conn.add(dn, object_class, attribute)

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




ldap_cli = LdapCli('ldap://127.0.0.1:389', 'dc=waylonglong,dc=com', 'admin', 'ldap123')
