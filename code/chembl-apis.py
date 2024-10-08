from fastapi import FastAPI
from db_model.basic_info.basic_info import smiles_from_compound_name, smiles_from_chembl_id, chembl_id_from_chebi
from db_model.compound_info.compound_info import compound_information_from_smiles
from db_model.experimental_data.activity import active_compound_from_target_id
from db_model.experimental_data.assay import find_all_drugmatrix, find_single_drugmatrix
from db_model.target_info import (compound_tested_against_target_id, 
                                  compound_tested_against_target_id_extended, 
                                  mechanism_target_from_name)

app = FastAPI()


@app.get("/compound_info_from_smiles")
def compound_info_from_smiles(smiles: str):
    """_summary_

    Args:
        compound_name (str): _description_

    Returns:
        _type_: _description_
    """    
    response = compound_information_from_smiles(smiles=smiles)
    #print(f"response: {response}")
    return response


@app.get("/compound_tested_against_target_extended")
def compound_tested_against_target_extended(target_chemb_id: str):
    """_summary_

    Args:
        compound_name (str): _description_

    Returns:
        _type_: _description_
    """    
    response = compound_tested_against_target_id_extended(target_chemb_id=target_chemb_id)
    #print(f"response: {response}")
    return response


@app.get("/compound_tested_against_target")
def compound_tested_against_target(target_chemb_id: str):
    """_summary_

    Args:
        compound_name (str): _description_

    Returns:
        _type_: _description_
    """    
    response = compound_tested_against_target_id(target_chemb_id=target_chemb_id)
    #print(f"response: {response}")
    return response


@app.get("/all_drug_matrix")
def all_drug_matrix(word: str='DRUGMATRIX'):
    """_summary_

    Args:
        compound_name (str): _description_

    Returns:
        _type_: _description_
    """    
    response = find_all_drugmatrix(word=word)
    #print(f"response: {response}")
    return response


@app.get("/drug_matrix")
def drug_matrix(description: str):
    """_summary_

    Args:
        compound_name (str): _description_

    Returns:
        _type_: _description_
    """    
    response = find_single_drugmatrix(description=description)
    #print(f"response: {response}")
    return response


@app.get("/mechanism_target")
def mechanism_target(compound_name: str):
    """_summary_

    Args:
        compound_name (str): _description_

    Returns:
        _type_: _description_
    """    
    response = mechanism_target_from_name(compound_name=compound_name)
    #print(f"response: {response}")
    return response


@app.get("/smiles_from_compound_name")
def smiles_from_name(compound_name: str):
    """_summary_

    Args:
        compound_name (str): _description_

    Returns:
        _type_: _description_
    """    
    response = smiles_from_compound_name(compound_name=compound_name)
    print(f"response: {response}")
    return response


@app.get("/smiles_from_chembl_id")
def smiles_from_id(chembl_ID: int):
    """ 
        This function return smiles string regarding chembl SQL queries, 
        which contain chembl_id
    
        input (str): 'CHLOROQUINE'
        output (str): 'CCN(CC)CCCC(C)Nc1ccnc2cc(Cl)ccc12' 
    """
    response = smiles_from_chembl_id(chembl_ID=chembl_ID)
    
    return response


@app.get("/chembl_id_from_chebi")
def chembl_from_chebi(chebi: int): 
    """_summary_

    Args:
        chebi (int): _description_

    Returns:
        _type_: _description_
    """    
    response = chembl_id_from_chebi(chebi=chebi)
    
    return response


@app.get("/active_compound_from_target_id")
def active_compound(
                    target_chemb_id: str, 
                    activity_value: float=1000.0, 
                    standard_type: str='IC50',
                    standard_units: str='nM',
                    ):
    """_summary_

    Args:
        target_chemb_id (str): _description_
        activity_value (float, optional): _description_. Defaults to 1000.0.
        standard_type (str, optional): _description_. Defaults to 'IC50'.
        standard_units (str, optional): _description_. Defaults to 'nM'.

    Returns:
        _type_: _description_
    """    
    response = active_compound_from_target_id(target_chemb_id=target_chemb_id,
                                              activity_value=activity_value,
                                              standard_type=standard_type,
                                              standard_units=standard_units)
    
    return response


















