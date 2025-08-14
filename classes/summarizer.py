class Summarizer:
    supported_event_types = {
        'PushEvent',
        'IssuesEvent',
        'WatchEvent',
    }

    @staticmethod
    def summarize(events: list) -> None:
        pushes: dict[str, int] = dict()
        issues: dict[str, dict[str, int]] = dict()
        watches: list[str] = list()
        for event in events:
            if event['type'] in Summarizer.supported_event_types:
                repo_name = event['repo']['name']
                match event['type']:
                    case 'PushEvent':
                        pushes[repo_name] = pushes.get(repo_name, 0) + 1
                    case 'IssuesEvent':
                        action = event['payload']['action']
                        dest = issues.get(action, dict())
                        dest[repo_name] = dest.get(action, {repo_name: 0})[repo_name] + 1
                        issues[action] = dest

                    case 'WatchEvent':
                        watches.append(repo_name)

        summary = ""

        summary += f'Pushed:\n'
        if pushes.__len__() > 0:
            for repo_name, count in pushes.items():
                summary += f'- {count} commits to {repo_name}\n'

        if issues.__len__() > 0:
            summary += f'Issues:\n'
            for action, repos in issues.items():
                summary += f'- {action}:\n'
                for repo_name, count in repos.items():
                    summary += f'\t{count} issues in {repo_name}\n'

        if watches.__len__() > 0:
            summary += f'Watched:\n'
            for repo_name in watches:
                summary += f'- {repo_name}\n'

        print(summary)