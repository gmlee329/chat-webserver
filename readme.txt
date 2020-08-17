flask와 python을 사용하여 webserver를 구축하였습니다.
vm상에서 ubuntu linux 환경에서 작업하였습니다.
챗봇을 만들어본 경험은 없어서 간단하게 질의 할 수 있는 질문을 지정해 놓고 해당 질문을 REST API를 통해 웹서버에 전달하고 해당하는 답변을 받아 출력해주는 방식으로 구현하였습니다.
클라이언트 프로그램은 웹서버로부터 질문 가능한 질문 리스트를 GET으로 요청하여 보여주고, 해당 질문을 질의하면 url의 parameter로 파싱하여 웹서버에 답변을 요청하는 방식으로 python 스크립트를 작성하였습니다.
docker와 kubernetes는 linux 로컬 디렉터리에 설치 후 해당 웹서버를 Dockerfile로 이미지를 만들고 컨테이너화 하였습니다. 
kubernetes는 kubeadm을 통해 구축하려고 했으나 vm환경이라 "The connection to the server localhost:8080 was refused"라는 오류가 고쳐지지 않아 kubernetes 공식 문서를 참조한 결과 minikube를 통해 환경 구축을 하여야한다는 해결 방법을 통해 구축하였습니다.
