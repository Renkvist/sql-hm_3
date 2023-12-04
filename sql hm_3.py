import sqlite3
conn = sqlite3.connect(':memory:')
c = conn.cursor()

# Створення таблиць
c.execute("""CREATE TABLE IF NOT EXISTS creature
	(creature_id INTEGER,
	creature_name TEXT,
	creature_species TEXT,
	creature_age VARCHAR)""")

c.execute("""CREATE TABLE IF NOT EXISTS armor
	(armor_id INTEGER,
	armor_name TEXT,
	armor_type INTEGER,
	armor_material TEXT)""")

c.execute("""CREATE TABLE IF NOT EXISTS weapon
	(weapon_id INTEGER,
	weapon_name TEXT,
	weapon_type INTEGER,
	weapon_material TEXT,
	hand_used INTEGER)""")

c.execute("""CREATE TABLE IF NOT EXISTS equipment
	(armor_id INTEGER,
	weapon_id INTEGER,
	set_bonus INTEGER,
	creature_id INTEGER)""")

# Створення даних для таблиць
creatures = [(96, 'Goliath', 'cyclops', '200+'),
(39, 'Jyrik Gauldurson', 'draugr', '500+'),
(20, 'Gimli', 'dwarf', '139')]

armors = [(231696, 'Enormous Steel Helmet', 'Hard', 'Iron'),
(252339, 'Ancient Nord Plate Armor', 'Hard', 'Steel'),
(261220, 'Erebor Helmet', 'Hard', 'Dwarwen Steel'),
(263220, 'Erebor Gauntlents', 'Medium', 'Dwarven Steel')]

weapons = [(117696, 'Mill log', 'Greathammer', 'Wood', 4),
(152339, 'Jyrik\'s Reaper', 'Sword', 'Steel', 2),
(166220, 'Erebor Greataxe', 'Greataxe', 'Dwarven Steel', 4),
(152358, 'Altair\'s sword', 'Sword', 'Steel', 2)]

set_bonuses = [(231696, 117696, 20, 96),
(252339, 152339, 30, 39),
(261220, 166220, 15, 20),
(263220, 166220, 10, 20)]

# Завантаження даних у таблиці
c.executemany("""INSERT INTO creature VALUES
	(?, ?, ?, ?)""", creatures)

c.executemany("""INSERT INTO armor VALUES
	(?, ?, ?, ?)""", armors)

c.executemany("""INSERT INTO weapon VALUES
	(?, ?, ?, ?, ?)""", weapons)

c.executemany("""INSERT INTO equipment VALUES
	(?, ?, ?, ?)""", set_bonuses)

# Вивід усіх даних з усіх таблиць
for row in c.execute('SELECT * FROM creature'):
	print(row)
for row in c.execute('SELECT * FROM armor'):
	print(row)
for row in c.execute('SELECT * FROM weapon'):
	print(row)
for row in c.execute('SELECT * FROM equipment'):
	print(row)

# Виконання запитів із ДЗ 2
c.execute("""SELECT armor.armor_name, equipment.set_bonus
FROM armor JOIN equipment
ON armor.armor_id = equipment.armor_id""")
print(c.fetchall())

c.execute("""SELECT creature.creature_name, creature.creature_species, equipment.set_bonus
FROM creature LEFT JOIN equipment
ON creature.creature_id = equipment.creature_id""")
print(c.fetchall())

# Зміна даних
c.execute("""UPDATE equipment SET set_bonus = 25 WHERE creature_id = 39""")
c.execute("""UPDATE creature SET creature_name = 'Draugr Deathlord', creature_id = 38 WHERE creature_id = 39""")

# Виконання запитів із ДЗ 2 після зміни даних
c.execute("""SELECT armor.armor_name, equipment.set_bonus
FROM armor JOIN equipment
ON armor.armor_id = equipment.armor_id""")
print(c.fetchall())

c.execute("""SELECT creature.creature_name, creature.creature_species, equipment.set_bonus
FROM creature LEFT JOIN equipment
ON creature.creature_id = equipment.creature_id""")
print(c.fetchall())


# Збереження змін та закриття з'єднання
conn.commit()
conn.close()