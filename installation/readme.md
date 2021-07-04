## installation of minimised CogStack-SemEHR and nlp2phenome
**NB: no need to clone repos by yourself, the script will checkout the most relevant branches**

1. download the two files into your computer
   ```bash
   # bash script for installation
   https://github.com/CogStack/CogStack-SemEHR/blob/safehaven_mini/installation/install_semehr.sh
   
   # semehr configuration template
   https://github.com/CogStack/CogStack-SemEHR/blob/safehaven_mini/installation/semehr_conf_template.json
   ```

2. run the downloaded bash script
   ```bash
   sh install_semehr.sh
   ```
   It will ask for a full path to install relevant software. All packages and repos will be installed there.

3. folder structure
   When it is installed successfully, the installation folder will contain the following folders.
   ```
   gcp - contains Java based NLP core software packages
   semehr - contains two Github repos of NLP and machine learning modules
   data - the working folder, which contains the following subfolders
        - input_docs: the free text documents to be analysed
        - output_docs: the NLP raw outputs
        - semehr_results: the semehr post processed results
        - phenome_results: the text phenotyping results
   ```

## run semehr
1. run nlp
   ```bash
   cd $install_path/semehr/CogStack-SemEHR
   python semehr_processor.py ../../data/semehr_settings.json
   ```
results will be saved to ` $install_path/data/semehr_results`

2. [optional] run phenotype computing for stroke, for example
   ```bash
   cd $install_path/semehr/nlp2phenome
   python predict_helper.py ./pretrained_models/stroke_settings/prediction_task.json
   python doc_inference.py ./pretrained_models/stroke_settings/doc_infer.json
   ```
   reulsts will be saved to `$install_path/data/phenome_results`
3. [optional] use customised document level rules
   - goto `cd $install_path/semehr/nlp2phenome`
   - edit `./pretrained_models/stroke_settings/prediction_task.json`. Change the `rule_file` to a customised rule file, for example using `$install_path/semehr/nlp2phenome/settings/stroke-subtype-rules-full.json`.
