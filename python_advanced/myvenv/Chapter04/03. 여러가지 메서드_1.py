class Unit:
  """
  인스턴스 속성 : 이름, 체력, 방어막, 공격력
  클래스 속성 : 전체 유닛 개수
  """
  count = 0
  def __init__(self, name, hp, shield, demege):
    self.name = name 
    self.__hp = hp
    self.shield = shield
    self.demege = demege
    Unit.count += 1
    print(f"[{self.name}](이)가 생성 되었습니다.")

    def __str__(self):
      return f"[{self.name}] 체력: {self.__hp} 방어막: {self.shield} 공격력: {self.demege}" 

      # 인스턴스 메서드 (instance method)
      # 인스턴스 속성에 접근할 수 있는 메서드
      def hit(self, demege):
        # 방어막 변경
        if self.shield >= demege:
          self.seield -= demege
          demege = 0
        else:
          demege -= self.shield
          self.shield = 0

        # 체력 변경
        if demege > 0:
          if self.hp > demege:
            self.hp -= demege
          else:
            self.hp = 0
      
      # 클래스 메서드 (class method)
      # 클래스 속성에 접근하는 메서드
      @classmethod
      def print_count(cls):
        print(f"생성된 유닛 개수 : [{cls.count}]개")

probe = Unit("프로브", 20, 20, 5)
zealot = Unit("질럿", 100, 60, 16)
dragoon = Unit("드라군", 100, 80, 20)

probe.hit(16)
print(probe)
probe.hit(16)
print(probe)
probe.hit(16)
print(probe)

Unit.print_count()