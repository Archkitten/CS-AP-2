package csa.week5;
import java.util.List;

public class MultipleGroup implements NumberGroup {
    private List<NumberGroup> groupList;

    public boolean contains(int n) {
        for (NumberGroup i : groupList) {
            if (i.contains(n)) {
                return true;
            }
        }
        return false;
    }
}
