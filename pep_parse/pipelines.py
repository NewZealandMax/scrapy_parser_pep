import csv
from datetime import datetime as dt
from pathlib import Path


BASE_DIR = Path(__file__).absolute().parent


class PepParsePipeline:

    def open_spider(self, spider):
        self.statuses = {}
        self.pep_count = 0

    def process_item(self, item, spider):
        status = item['status']
        self.statuses[status] = self.statuses.get(status, 0) + 1
        self.pep_count += 1
        return item

    def close_spider(self, spider):
        results = [('Статус', 'Количество')]
        results.extend(sorted(self.statuses.items()))
        results.append(('Total', self.pep_count))

        current_time = dt.now().strftime('%Y_%m_%d_%H_%M_%S')
        dir_path = BASE_DIR / '../results'
        file_path = dir_path / f'status_summary_{current_time}.csv'
        with open(file_path, 'w', encoding='utf-8') as file:
            writer = csv.writer(file, dialect='unix')
            writer.writerows(results)
