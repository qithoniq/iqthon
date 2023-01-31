FROM jepthoniq/jepthon:slim-buster

#clonning repo 

RUN git clone https://github.com/qithoniq/qithon /root/qithon

#working directory 

WORKDIR /root/qithon

RUN apk add --update --no-cache p7zip

# Install requirements

RUN pip3 install --no-cache-dir -r requirements.txt

ENV PATH="/home/qithon/bin:$PATH"

CMD ["python3","-m","qithon"]

