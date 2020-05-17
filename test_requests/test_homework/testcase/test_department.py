from test_requests.test_homework.api.department import Department


class TestDepartment:
    def setup(self):
        self.depart = Department()

    # 测试获取token是否成功
    def test_get_access_token(self):
        r = self.depart.get_access_token()
        assert r["errcode"] == 0

    # 测试获取部门列表
    def test_depart_select(self):
        r = self.depart.select_depart()
        assert r["errcode"] == 0

    # 测试创建部门
    def test_depart_create(self):
        r = self.depart.create_depart("家庭作业")
        print(self.test_depart_select())
        assert r["errcode"] == 0

    # 测试更新部门
    def test_depart_update(self):
        r = self.depart.update_depart(id=3, name="家庭作业1")
        print(self.test_depart_select())
        assert r["errcode"] == 0

    # 测试删除部门
    def test_depart_delete(self):
        r = self.depart.delete_depart(id=3)
        print(self.test_depart_select())
        assert r["errcode"] == 0
