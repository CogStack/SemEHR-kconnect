import utils
import sqldbutils as dutil

# query concept sql
autoimmune_concepts_sql = """
select distinct concept_name from [SQLCRIS_User].[Kconnect].[ulms_concept_mapping]
"""

# query patient sql
patients_sql = """
select brcid, primary_diag, diagnosis_date, dob, gender_id, enthnicitycleaned from [SQLCRIS_User].[Kconnect].[treatment_res_dep]
"""

# query concept freqs over patient
autoimmune_sympton_freq_sql = """
"""


def read_data(rows, container):
    container += [r.__dict__ for r in rows]


def get_concepts(output_file):
    autoimmune_concepts = []
    patients = []
    dutil.squery_data(autoimmune_concepts_sql, read_data, autoimmune_concepts)
    dutil.squery_data(autoimmune_concepts_sql, read_data, patients)
    # patient dic
    patient_dic = {}
    for p in patients:
        patient_dic[p['BrcId']] = p

    for c in autoimmune_concepts:
        sympton_freq_result = []
        dutil.squery_data(autoimmune_sympton_freq_sql, read_data, sympton_freq_result)
        for sf in sympton_freq_result:
            patient_dic[sf['BrcId']][c] = sf['num']
    s = '\t'.join([k for k in patients[0]] + autoimmune_concepts) + '\n'
    for p in patients:
        s += '\t'.join([p[k] for k in p] + ['-' if c in p else p[c] for c in autoimmune_concepts]) + '\n'
    utils.save_string(s, output_file)

