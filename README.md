# Pdf To Audio
Simple pdf to audio converter with some customizable settings 

#### TODOs
- [ ] Get GUI working with Docker
- [ ] Take in pdf input
- [ ] Change voice
- [ ] Change speed
- [ ] Change download to location  


#### Local setup

1. Clone the repository and cd into it 
   
   ```BASH 
    → https://github.com/ari-hacks/pdf-to-audio.git
    → cd pdf-to-audio
   ```
2. Pipenv dependency management

    ```BASH 
    #updating pipenv
    ➜ pip install pipenv --upgrade
    ```
    ```BASH
    #run pipenv 
    → pipenv shell
    #install dependencies  
    → pipenv install
    ```

#### Build with Docker 

1. Build Docker image 
   ```BASH 
   → docker build -t pdf-to-audio .
   ```

2. Run Image

    ```BASH
    → docker run pdf-to-audio
    ```