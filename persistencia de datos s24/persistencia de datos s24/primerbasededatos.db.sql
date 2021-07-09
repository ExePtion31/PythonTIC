BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "consumidores" (
	"id"	INTEGER,
	"Name"	TEXT,
	"Email"	TEXT,
	"grado"	TEXT
);
CREATE TABLE IF NOT EXISTS "basedatospaises" (
	"CODIGO"	TEXT,
	"PAIS"	TEXT,
	"CONTINENTE"	TEXT
);
INSERT INTO "basedatospaises" VALUES ('AFG','Afghanistan','Asia');
INSERT INTO "basedatospaises" VALUES ('NLD','Netherlands','Europa');
INSERT INTO "basedatospaises" VALUES ('ALB','Albania','Europa');
COMMIT;
