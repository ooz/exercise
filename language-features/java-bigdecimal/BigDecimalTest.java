import java.math.BigDecimal;

/**
 * 0.1 cannot exactly be represented as double floating point
 */
public class BigDecimalTest {
    public static void main(String[] args) {

        test_valueOf();

        test_one_to_hundred_percent_calculations_are_equal();
    }

    private static void test_valueOf() {
        BigDecimal fromDouble = new BigDecimal(0.1);
        BigDecimal fromString = new BigDecimal("0.1");
        BigDecimal fromValueOfDouble = BigDecimal.valueOf(0.1);
        Double doubleFromString = new Double("0.1");
        Double doubleFromDouble = new Double(0.1);

        System.out.println(fromDouble);
        System.out.println(fromString);
        System.out.println(fromValueOfDouble);

        System.out.println(doubleFromString);
        System.out.println(doubleFromDouble.doubleValue());

        assert fromValueOfDouble.compareTo(fromDouble) != 0;
        // but...
        assert fromValueOfDouble.doubleValue() == 0.1d;
        assert fromDouble.doubleValue() == 0.1d;

        assert fromValueOfDouble.compareTo(fromString) == 0;
        assert doubleFromDouble.doubleValue() == 0.1d;
        assert doubleFromString.doubleValue() == doubleFromDouble.doubleValue();
    }

    private static void test_one_to_hundred_percent_calculations_are_equal() {
        for (int percentValue = 0; percentValue <= 100; percentValue++) {
            BigDecimal fromFloat = calculateInFloat(percentValue);
            BigDecimal asBigDecimal = calculateInBigDecimal(percentValue);

            assert fromFloat.compareTo(asBigDecimal) == 0;
        }
    }

    private static BigDecimal calculateInFloat(int percentValue) {
        return BigDecimal.valueOf(percentValue / 100.0 * -1);
    }

    private static BigDecimal calculateInBigDecimal(int percentValue) {
        return BigDecimal.valueOf(percentValue)
            .divide(BigDecimal.valueOf(100.0))
            .multiply(BigDecimal.valueOf(-1));
    }
}
