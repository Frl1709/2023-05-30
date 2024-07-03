from database.DB_connect import DBConnect
from model.team import Team


class DAO:

   @staticmethod
   def getTeams():
      conn = DBConnect.get_connection()
      result = []
      cursor = conn.cursor(dictionary=True)
      query = """select ID, year, teamCode, name
              from teams t
               group by name"""

      cursor.execute(query, )
      for row in cursor:
         result.append(Team(**row))

      cursor.close()
      conn.close()
      return result

   @staticmethod
   def getNodes(nome):
       conn = DBConnect.get_connection()
       result = []
       cursor = conn.cursor(dictionary=True)
       query = """select distinct(year)
                    from teams t
                    where t.name = %s """

       cursor.execute(query, (nome,))
       for row in cursor:
           result.append(row['year'])

       cursor.close()
       conn.close()
       return result

   @staticmethod
   def getEdge(nome):
       conn = DBConnect.get_connection()
       result = []
       cursor = conn.cursor(dictionary=True)
       query = """select a1, a2, count(*) as peso
                    from (select a.`year` as a1, t.ID as id1, t.name as n1, a.playerID as p1 
                            from appearances a, teams t 
                            where t.name = %s and t.ID = a.teamID) t1,
                        (select a.`year` as a2, t.ID as id2, t.name as n2, a.playerID as p2 
                            from appearances a, teams t 
                            where t.name = %s and t.ID = a.teamID) t2
                    where p1 = p2 and a1 < a2
                    group by a1, a2"""

       cursor.execute(query, (nome, nome, ))
       for row in cursor:
           result.append((row['a1'],
                          row['a2'],
                          row['peso']))

       cursor.close()
       conn.close()
       return result