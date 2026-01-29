#!/bin/sh

PROJECT_NAME="ai-ebook-generator"

echo "Criando estrutura do projeto: $PROJECT_NAME"

# Diret√≥rios
mkdir -p "$PROJECT_NAME"
mkdir -p "$PROJECT_NAME/prompts"
mkdir -p "$PROJECT_NAME/src"
mkdir -p "$PROJECT_NAME/examples"
mkdir -p "$PROJECT_NAME/output"

# Arquivos principais
touch "$PROJECT_NAME/README.md"
touch "$PROJECT_NAME/requirements.txt"
touch "$PROJECT_NAME/.gitignore"

# Prompts
touch "$PROJECT_NAME/prompts/indice_prompt.md"
touch "$PROJECT_NAME/prompts/capitulo_prompt.md"
touch "$PROJECT_NAME/prompts/capa_prompt.md"

# C√≥digo
touch "$PROJECT_NAME/src/ebook_generator.py"

# Exemplos
touch "$PROJECT_NAME/examples/ebook_exemplo.md"

# Conte√∫do do requirements.txt
cat <<EOF > "$PROJECT_NAME/requirements.txt"
openai
python-dotenv
EOF

# Conte√∫do do .gitignore
cat <<EOF > "$PROJECT_NAME/.gitignore"
.env
__pycache__/
output/*.pdf
EOF

echo "Estrutura criada com sucesso Ì∫Ä"

