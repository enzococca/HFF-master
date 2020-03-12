CREATE VIEW hff_quote_view AS
 SELECT hff_quote.sito_q, hff_quote.area_q, hff_quote.us_q, hff_quote.unita_misu, hff_quote.quota_q, hff_quote.geometry, us_table.id_us, us_table.sito, us_table.area, us_table.us, us_table.struttura, us_table.definizione_stratigrafica, us_table.definizione_interpretativa, us_table.descrizione, us_table.interpretazione, us_table.rapporti, us_table.periodo_iniziale, us_table.fase_iniziale, us_table.periodo_finale, us_table.fase_finale, us_table.anno_scavo
   FROM hff_quote
   JOIN us_table ON hff_quote.sito_q = us_table.sito AND hff_quote.area_q = us_table.area AND hff_quote.us_q = us_table.us;


CREATE VIEW hff_us_view AS SELECT pyunitastratigrafiche.PK_UID, pyunitastratigrafiche.geometry, pyunitastratigrafiche.tipo_us_s, pyunitastratigrafiche.scavo_s, pyunitastratigrafiche.area_s, pyunitastratigrafiche.us_s, us_table.id_us, us_table.sito, us_table.area, us_table.us, us_table.struttura, us_table.definizione_stratigrafica, us_table.definizione_interpretativa, us_table.descrizione, us_table.interpretazione, us_table.rapporti, us_table.periodo_iniziale, us_table.fase_iniziale, us_table.periodo_finale, us_table.fase_finale, us_table.anno_scavo
   FROM pyunitastratigrafiche
   JOIN us_table ON pyunitastratigrafiche.scavo_s = us_table.sito AND pyunitastratigrafiche.area_s = us_table.area AND pyunitastratigrafiche.us_s = us_table.us

CREATE VIEW hff_uscaratterizzazioni_view AS
 SELECT pyuscaratterizzazioni.geometry, pyuscaratterizzazioni.tipo_us_c, pyuscaratterizzazioni.scavo_c, pyuscaratterizzazioni.area_c, pyuscaratterizzazioni.us_c, us_table.sito, us_table.id_us, us_table.area, us_table.us, us_table.struttura, us_table.definizione_stratigrafica, us_table.definizione_interpretativa, us_table.descrizione, us_table.interpretazione, us_table.rapporti, us_table.periodo_iniziale, us_table.fase_iniziale, us_table.periodo_finale, us_table.fase_finale, us_table.anno_scavo
   FROM pyuscaratterizzazioni
   JOIN us_table ON pyuscaratterizzazioni.scavo_c = us_table.sito AND pyuscaratterizzazioni.area_c = us_table.area AND pyuscaratterizzazioni.us_c = us_table.us;

/*
CREATE VIEW hff_us_view AS SELECT pyunitastratigrafiche.PK_UID, pyunitastratigrafiche.geometry, pyunitastratigrafiche.tipo_us_s, pyunitastratigrafiche.scavo_s, pyunitastratigrafiche.area_s, pyunitastratigrafiche.us_s, us_table.id_us, us_table.sito, us_table.area, us_table.us, us_table.struttura, us_table.definizione_stratigrafica, us_table.definizione_interpretativa, us_table.descrizione, us_table.interpretazione, us_table.rapporti, us_table.periodo_iniziale, us_table.fase_iniziale, us_table.periodo_finale, us_table.fase_finale, us_table.anno_scavo
   FROM pyunitastratigrafiche
   JOIN us_table ON pyunitastratigrafiche.scavo_s = us_table.sito AND pyunitastratigrafiche.area_s = us_table.area AND pyunitastratigrafiche.us_s = us_table.us
*/






