import logging
from python_logging_rabbitmq import RabbitMQHandler
from config import Settings


def main() -> None:
    settings = Settings()
    rabbitmq_handler = RabbitMQHandler(
        host=settings.RABBITMQ_HOST,
        port=settings.RABBITMQ_PORT,
        username=settings.RABBITMQ_USER,
        password=settings.RABBITMQ_PASSWORD,
        exchange='logs',
        exchange_type='direct',
        routing_key='test',
        durable=True)
    logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',datefmt='%Y-%m-%d %H:%M:%S',handlers=[rabbitmq_handler])
    logging.info('test info')
    logging.debug('test debug')
    logging.warning('test warning')

if __name__ == "__main__":
    main()
